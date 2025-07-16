#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Curation vs Retrieval Experiment Comparison
# ==========================================
# This notebook compares the performance of three models (gpt-4.1, o4-mini, Qwen3-32B)
# across two datasets (nlp4lp, nlp4opt) using both curation and retrieval methods.

# Import core libraries with compatibility checks
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import json
import re
from collections import defaultdict
import warnings

# Check for potential compatibility issues
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"Pandas version: {pd.__version__}")

# Suppress common warnings that might cause issues
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=RuntimeWarning)

# Add numpy array compatibility fix
def safe_array_convert(data):
    """
    Safely convert data to numpy array, handling type conversion issues.
    """
    try:
        if hasattr(data, 'values'):
            # Pandas Series/DataFrame
            return np.asarray(data.values, dtype=np.float64)
        elif isinstance(data, (list, tuple)):
            return np.asarray(data, dtype=np.float64)
        elif isinstance(data, np.ndarray):
            return np.asarray(data, dtype=np.float64)
        else:
            return np.asarray(data, dtype=np.float64)
    except Exception as e:
        print(f"⚠️  Array conversion warning: {e}")
        try:
            return np.array(data, dtype=object)
        except:
            return np.array([])

# Monkey patch to fix numpy array issues
original_asarray = np.asarray
def patched_asarray(data, *args, **kwargs):
    try:
        return original_asarray(data, *args, **kwargs)
    except (TypeError, ValueError) as e:
        if "Cannot convert" in str(e) and "numpy.ndarray" in str(e):
            return safe_array_convert(data)
        else:
            raise e

np.asarray = patched_asarray

# Additional safeguards for matplotlib array handling
def safe_matplotlib_conversion(func):
    """
    Decorator to handle matplotlib numpy array conversion errors.
    """
    def wrapper(*args, **kwargs):
        try:
            # Convert any numpy arrays to safe format
            safe_args = []
            for arg in args:
                if hasattr(arg, '__array__') or isinstance(arg, np.ndarray):
                    safe_args.append(safe_array_convert(arg))
                else:
                    safe_args.append(arg)
            
            safe_kwargs = {}
            for key, value in kwargs.items():
                if hasattr(value, '__array__') or isinstance(value, np.ndarray):
                    safe_kwargs[key] = safe_array_convert(value)
                else:
                    safe_kwargs[key] = value
                    
            return func(*safe_args, **safe_kwargs)
        except Exception as e:
            if "Cannot convert numpy.ndarray" in str(e):
                print(f"Handled numpy array conversion in {func.__name__}")
                # Try with basic Python types
                basic_args = []
                for arg in args:
                    if hasattr(arg, '__iter__') and not isinstance(arg, str):
                        basic_args.append(list(arg))
                    else:
                        basic_args.append(arg)
                return func(*basic_args, **{k: v for k, v in kwargs.items() if not hasattr(v, '__array__')})
            else:
                raise e
    return wrapper

print("Advanced numpy array conversion protection loaded")

# Set matplotlib backend to avoid display issues
try:
    matplotlib.use('Agg')  # Use non-interactive backend
    print("Using Agg backend for matplotlib")
except:
    print("Could not set matplotlib backend")

# Try to import seaborn with comprehensive error handling
try:
    # Check scipy compatibility first
    try:
        import scipy
        print(f"SciPy version: {scipy.__version__}")
    except ImportError:
        print("SciPy not available - some seaborn features may be limited")
    
    import seaborn as sns
    SEABORN_AVAILABLE = True
    print("Seaborn imported successfully")
    
    # Test seaborn basic functionality
    try:
        sns.set_theme()  # Test if seaborn works without errors
        print("Seaborn theme set successfully")
    except Exception as e:
        print(f"⚠️  Seaborn theme error: {e}")
        SEABORN_AVAILABLE = False
        
except (ImportError, ValueError, Exception) as e:
    SEABORN_AVAILABLE = False
    print(f"Seaborn not available ({type(e).__name__}: {e}) - using matplotlib only")

# Create fallback seaborn object if needed
if not SEABORN_AVAILABLE:
    class DummySeaborn:
        def __init__(self):
            self.__version__ = "fallback"
            
        def set_palette(self, *args, **kwargs):
            pass
            
        def set_theme(self, *args, **kwargs):
            pass
            
        def heatmap(self, data, *args, **kwargs):
            # Extract the axis if provided
            ax = kwargs.get('ax', plt.gca())
            try:
                # Use matplotlib's imshow as fallback with safe array conversion
                if hasattr(data, 'values'):
                    data_array = safe_array_convert(data.values)
                else:
                    data_array = safe_array_convert(data)
                
                im = ax.imshow(data_array, cmap=kwargs.get('cmap', 'viridis'), aspect='auto')
                return im
            except Exception as e:
                print(f"Fallback heatmap error: {e}")
                return None
                
    sns = DummySeaborn()

# Import functions from accuracy_analyzer
from accuracy_analyzer import analyze_accuracy

# Set up plotting
# get_ipython().run_line_magic('matplotlib', 'inline')

# Configure matplotlib style
if SEABORN_AVAILABLE:
    try:
        plt.style.use('seaborn-v0_8')
        print("Using seaborn-v0_8 style")
    except OSError:
        try:
            plt.style.use('seaborn')
            print("Using seaborn style")
        except OSError:
            plt.style.use('default')
            print("Using default style - seaborn styles not available")
else:
    plt.style.use('default')
    print("Using matplotlib default style")

plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Set color palette
if SEABORN_AVAILABLE:
    try:
        sns.set_palette("husl")
        print("Seaborn palette set")
    except:
        print("Could not set seaborn palette - using matplotlib defaults")
else:
    # Set matplotlib color cycle as fallback
    plt.rcParams['axes.prop_cycle'] = plt.cycler('color', 
        ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

print("Libraries imported successfully!")
print("Ready to analyze curation vs retrieval experiments...")


# In[6]:


# Additional Safe Plotting Functions
# ===================================

def safe_bar_plot(ax, x, y, **kwargs):
    """
    Safe bar plotting with array conversion to prevent numpy.ndarray errors.
    """
    try:
        # Convert to safe arrays
        x_safe = list(x) if not isinstance(x, (list, tuple, range)) else list(x)
        y_safe = safe_array_convert(y)
        
        # Handle yerr parameter specially
        if 'yerr' in kwargs:
            yerr_safe = safe_array_convert(kwargs['yerr'])
            kwargs['yerr'] = yerr_safe
            
        return ax.bar(x_safe, y_safe, **kwargs)
    except Exception as e:
        print(f"Bar plot error: {e}")
        # Ultra-safe fallback
        try:
            safe_kwargs = {k: v for k, v in kwargs.items() if k != 'yerr'}
            y_list = [float(val) for val in y]
            return ax.bar(range(len(y_list)), y_list, **safe_kwargs)
        except:
            return None

def safe_imshow(ax, data, **kwargs):
    """
    Safe imshow with array conversion to prevent numpy.ndarray errors.
    """
    try:
        # Convert data to safe numpy array
        if hasattr(data, 'values'):
            data_safe = safe_array_convert(data.values)
        else:
            data_safe = safe_array_convert(data)
        
        return ax.imshow(data_safe, **kwargs)
    except Exception as e:
        print(f"Imshow error: {e}")
        return None

def safe_hist(ax, data, **kwargs):
    """
    Safe histogram plotting with array conversion.
    """
    try:
        data_safe = safe_array_convert(data)
        # Remove any NaN or inf values
        data_clean = data_safe[np.isfinite(data_safe)]
        return ax.hist(data_clean, **kwargs)
    except Exception as e:
        print(f"Histogram error: {e}")
        return None

def safe_plot(ax, x, y, **kwargs):
    """
    Safe line plotting with array conversion.
    """
    try:
        x_safe = safe_array_convert(x)
        y_safe = safe_array_convert(y)
        return ax.plot(x_safe, y_safe, **kwargs)
    except Exception as e:
        print(f"Plot error: {e}")
        return None

def safe_boxplot(ax, data, **kwargs):
    """
    Safe boxplot with array conversion.
    """
    try:
        if isinstance(data, list):
            data_safe = [safe_array_convert(d) for d in data]
        else:
            data_safe = safe_array_convert(data)
        return ax.boxplot(data_safe, **kwargs)
    except Exception as e:
        print(f"Boxplot error: {e}")
        return None

# Monkey patch matplotlib functions to use safe versions
def patch_matplotlib_functions():
    """
    Apply patches to prevent numpy array conversion errors.
    """
    try:
        # Store original functions
        if not hasattr(plt.Axes, '_original_bar'):
            plt.Axes._original_bar = plt.Axes.bar
            plt.Axes._original_imshow = plt.Axes.imshow
            plt.Axes._original_hist = plt.Axes.hist
            
        # Create safe wrapper functions
        def safe_bar_wrapper(self, x, height, **kwargs):
            return safe_bar_plot(self, x, height, **kwargs)
            
        def safe_imshow_wrapper(self, X, **kwargs):
            return safe_imshow(self, X, **kwargs)
            
        def safe_hist_wrapper(self, x, **kwargs):
            return safe_hist(self, x, **kwargs)
        
        # Apply patches
        plt.Axes.bar = safe_bar_wrapper
        plt.Axes.imshow = safe_imshow_wrapper  
        plt.Axes.hist = safe_hist_wrapper
        
        print("Matplotlib functions patched for numpy array safety")
        
    except Exception as e:
        print(f"Could not patch matplotlib functions: {e}")
        print("Will use manual safe functions instead")

# Apply the patches
patch_matplotlib_functions()

print("Safe plotting functions loaded successfully")


# In[7]:


def discover_experiment_files():
    """
    Auto-discover all experiment result files in the datasets directory.
    Returns a structured dictionary of experiment files.
    """
    datasets_dir = Path("datasets")
    
    # Check if datasets directory exists
    if not datasets_dir.exists():
        print(f"Datasets directory not found: {datasets_dir}")
        return {}
    
    experiment_files = defaultdict(lambda: defaultdict(dict))
    
    # Models to look for (with variations)
    model_patterns = {
        "gpt-4.1": ["gpt-4.1", "gpt4.1", "gpt-4"],
        "o4-mini": ["o4-mini", "o1-mini", "gpt-4o-mini"],
        "Qwen-Qwen3-32B": ["Qwen-Qwen3-32B", "Qwen3-32B", "qwen"]
    }
    
    datasets = ["nlp4lp", "nlp4opt"]
    
    print("Discovering experiment files...")
    print("=" * 50)
    
    # First, scan all subdirectories in datasets/
    for subdir in datasets_dir.iterdir():
        if not subdir.is_dir():
            continue
            
        dir_name = subdir.name.lower()
        print(f"Examining directory: {subdir}")
        
        # Try to identify dataset and model from directory name
        identified_dataset = None
        identified_model = None
        
        for dataset in datasets:
            if dataset in dir_name:
                identified_dataset = dataset
                break
        
        for model_key, model_variants in model_patterns.items():
            for variant in model_variants:
                if variant.lower().replace("-", "").replace(".", "") in dir_name.replace("-", "").replace(".", ""):
                    identified_model = model_key
                    break
            if identified_model:
                break
        
        if not identified_dataset or not identified_model:
            print(f"Could not identify dataset/model from directory name: {dir_name}")
            continue
        
        # Look for JSONL files in this directory
        jsonl_files = list(subdir.glob("*.jsonl"))
        if not jsonl_files:
            print(f"No JSONL files found in: {subdir}")
            continue
        
        print(f"Identified: {identified_dataset} + {identified_model}")
        
        # Process each JSONL file
        for jsonl_file in jsonl_files:
            file_name = jsonl_file.name.lower()
            
            # Determine if it's curation or retrieval
            method = "unknown"
            if "curation" in file_name or "curate" in file_name:
                method = "curation"
            elif "retrieval" in file_name or "retrieve" in file_name or "ret" in file_name:
                method = "retrieval"
            elif "kb" in file_name or "knowledge" in file_name:
                method = "curation"
            else:
                # Try to infer from file content
                method = infer_method_from_content(jsonl_file)
            
            if method != "unknown":
                experiment_files[identified_model][identified_dataset][method] = str(jsonl_file)
                print(f"{method}: {jsonl_file.name}")
            else:
                print(f"Could not determine method for: {jsonl_file.name}")
    
    return dict(experiment_files)

def infer_method_from_content(file_path, sample_size=5):
    """
    Infer experiment method by examining response formats in the file.
    Curation experiments typically have longer, more detailed responses.
    """
    try:
        with open(file_path, 'r') as f:
            total_response_length = 0
            count = 0
            
            for i, line in enumerate(f):
                if i >= sample_size:
                    break
                try:
                    data = json.loads(line)
                    response = str(data.get('agent_response', ''))
                    total_response_length += len(response)
                    count += 1
                except:
                    continue
            
            if count > 0:
                avg_length = total_response_length / count
                # If average response length > 100 chars, likely curation
                return "curation" if avg_length > 100 else "retrieval"
    except:
        pass
    
    return "unknown"

# Discover all experiment files
experiment_files = discover_experiment_files()

print(f"\nSummary:")
print(f"Found experiments for {len(experiment_files)} models")
for model, datasets in experiment_files.items():
    for dataset, methods in datasets.items():
        print(f"  {model} - {dataset}: {list(methods.keys())}")

if not experiment_files:
    print("No experiment files found. Please check your file structure.")
else:
    print(f"\nReady to analyze {sum(len(methods) for datasets in experiment_files.values() for methods in datasets.values())} experiment files")


# In[8]:


# Analyze all experiments
print("Starting simple analysis...")
if experiment_files:
    print("ACCURACY RESULTS")
    print("=" * 60)
    
    curation_results = []
    retrieval_results = []
    all_results = []
    
    for model in experiment_files:
        for dataset in experiment_files[model]:
            for method in experiment_files[model][dataset]:
                file_path = experiment_files[model][dataset][method]
                result = analyze_accuracy(file_path, threshold=1e-2)
                
                accuracy = float(str(result['accuracy_percentage']))
                
                print(f"✓ {model:>15} | {dataset:>8} | {method:>10} | {accuracy:6.2f}%")
                
                all_results.append({
                        'model': model,
                        'dataset': dataset,
                    'method': method,
                    'accuracy': accuracy
                })
                
                if method == 'curation':
                    curation_results.append(accuracy)
                elif method == 'retrieval':
                    retrieval_results.append(accuracy)
    
    # Simple summary
    print(f"\nSUMMARY")
    print("=" * 30)
    
    if curation_results:
        curation_avg = sum(curation_results) / len(curation_results)
        print(f"Curation:  {curation_avg:6.2f}% (n={len(curation_results)})")
    
    if retrieval_results:
        retrieval_avg = sum(retrieval_results) / len(retrieval_results)
        print(f"Retrieval: {retrieval_avg:6.2f}% (n={len(retrieval_results)})")
    
    if curation_results and retrieval_results:
        improvement = curation_avg - retrieval_avg
        print(f"Difference: {improvement:5.2f}% (Curation - Retrieval)")
        
        if improvement > 0:
            print("Curation performs better!")
        elif improvement < 0:
            print("Retrieval performs better!")
        else:
            print("No significant difference")
    
    print(f"\nAnalysis complete! Processed {len(all_results)} experiments.")
    
else:
    print("No experiment files found")

