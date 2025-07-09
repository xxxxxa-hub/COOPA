"""
Knowledge Base Initialization Tools
This module contains utilities for creating structured knowledge base directories
with predefined hierarchical organization for specific domains.
"""

import os
from pathlib import Path
from typing import List, Dict, Any


def create_or_knowledge_base(base_directory: str) -> str:
    """
    Initialize a comprehensive Operations Research knowledge base directory structure.
    
    Creates a hierarchical directory structure covering all major areas of Operations Research
    including Linear Programming, Integer Programming, Network Flows, Dynamic Programming,
    Nonlinear Programming, Metaheuristics, Decision Analysis, Stochastic Processes,
    Queuing Theory, Simulation, and Systems Dynamics.
    
    Args:
        base_directory (str): Path where the knowledge base directory should be created
        
    Returns:
        str: Success message with the path of the created knowledge base
        
    Raises:
        OSError: If directory creation fails
        PermissionError: If insufficient permissions to create directories
    """
    
    # Define the complete Operations Research knowledge structure
    or_structure = [
        "2.1. Operations Research",
        "2.1.1. Modeling approaches", 
        "2.1.2. Heuristic versus optimization procedures",
        "2.2. Linear Programming (LP)",
        "2.2.1. LP applications",
        "2.2.1.1. Diet problem",
        "2.2.1.2. Work scheduling", 
        "2.2.1.3. Capital budgeting",
        "2.2.1.4. Blending problems",
        "2.2.2. LP modeling techniques",
        "2.2.3. LP assumptions",
        "2.2.4. Simplex method",
        "2.2.5. Degenerate and unbounded solutions",
        "2.2.6. Post-optimality and sensitivity analysis",
        "2.2.7. Interior-point approaches", 
        "2.2.8. Duality theory",
        "2.2.9. Revised simplex method",
        "2.2.10. Dual simplex method",
        "2.2.11. Parametric programming",
        "2.2.12. Goal programming",
        "2.3. Transportation Problem",
        "2.3.1. Transportation model and its variants",
        "2.3.2. Transportation simplex method",
        "2.3.3. Transshipment problems",
        "2.4. Linear Assignment Problem",
        "2.4.1. Assignment model",
        "2.4.2. The Hungarian algorithm",
        "2.5. Network Flows and Optimization",
        "2.5.1. Shortest path problem",
        "2.5.2. Minimum spanning tree problem",
        "2.5.3. Maximum flow problem",
        "2.5.4. Minimum cost flow problem",
        "2.5.5. CPM and PERT problems",
        "2.5.6. Network simplex method",
        "2.6. Deterministic Dynamic Programming",
        "2.6.1. Applications",
        "2.6.1.1. Knapsack/fly-away/cargo-loading problems",
        "2.6.1.2. Workforce size problems",
        "2.6.1.3. Equipment replacement problems",
        "2.6.1.4. Investment problems",
        "2.6.1.5. Inventory (see Operations Engineering & Management knowledge area)",
        "2.6.2. Forward and backward recursions",
        "2.7. Integer Programming",
        "2.7.1. Applications and modeling techniques",
        "2.7.1.1. Capital budgeting",
        "2.7.1.2. Set-covering and set-partitioning problems",
        "2.7.1.3. Fixed-charge problem",
        "2.7.1.4. Either-or and if-then constraints",
        "2.7.2. Branch-and-bound algorithm",
        "2.7.3. Cutting plane algorithm",
        "2.7.4. Traveling salesman problem and solution methods",
        "2.8. Nonlinear Programming",
        "2.8.1. Unconstrained algorithms",
        "2.8.1.1. Direct search methods",
        "2.8.1.2. Gradient methods",
        "2.8.2. Constrained algorithms",
        "2.8.2.1. Separable programming",
        "2.8.2.2. Quadratic programming",
        "2.8.2.3. Chance-constrained programming",
        "2.8.2.4. Linear combinations method",
        "2.9. Metaheuristics",
        "2.9.1. Steepest ascent and descent (Greedy algorithms)",
        "2.9.2. Tabu search",
        "2.9.3. Simulated annealing",
        "2.9.4. Genetic algorithms",
        "2.9.5. Ant colony optimization",
        "2.9.6. Particle swarm techniques",
        "2.10. Decision Analysis and Game Theory",
        "2.10.1. Multi-criteria decision making",
        "2.10.2. Decision making under certainty",
        "2.10.2.1. Analytic hierarchy process",
        "2.10.2.2. ELECTRE",
        "2.10.3. Decision making under risk and uncertainty",
        "2.10.3.1. Decision tree-based expected value criterion",
        "2.10.3.2. Utility theory",
        "2.10.4. Two-person zero-sum and constant-sum games",
        "2.10.5. Robust decision making",
        "2.11. Modeling Under Uncertainty",
        "2.11.1. Stochastic processes",
        "2.11.2. Markov chains",
        "2.11.3. Chapman-Kolmogorov equations",
        "2.11.4. States and properties",
        "2.11.5. Stochastic programming",
        "2.12. Queuing Systems",
        "2.12.1. Components of a queuing model",
        "2.12.2. Relationship between the exponential and Poisson distributions",
        "2.12.3. Birth-and-death process-based queuing models",
        "2.12.4. Queuing models involving non-exponential distributions",
        "2.12.5. Priority-discipline queuing models",
        "2.12.6. Queuing networks",
        "2.13. Simulation",
        "2.13.1. Monte Carlo simulation",
        "2.13.2. Continuous and discrete time models",
        "2.13.3. Simulation methodology",
        "2.13.3.1. Sampling from probability distributions",
        "2.13.4. Random number generation",
        "2.14. Fundamentals of Systems Dynamics",
        "2.14.1. Principles of systems dynamics",
        "2.14.2. Balancing loops",
        "2.14.3. Feedback loops"
    ]
    
    try:
        # Create base directory
        base_path = Path(base_directory)
        base_path.mkdir(parents=True, exist_ok=True)
        
        # Parse structure and create directory tree
        directory_tree = _parse_hierarchical_structure(or_structure)
        
        # Create all directories
        created_dirs = []
        for dir_path in directory_tree:
            full_path = base_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(full_path.relative_to(base_path)))
            
        return (
            f"Successfully created Operations Research knowledge base at '{base_directory}' "
            f"with {len(created_dirs)} directories covering all major OR topics including: "
            f"Linear Programming, Integer Programming, Network Flows, Dynamic Programming, "
            f"Nonlinear Programming, Metaheuristics, Decision Analysis, Stochastic Modeling, "
            f"Queuing Theory, Simulation, and Systems Dynamics."
        )
        
    except PermissionError as e:
        raise PermissionError(f"Insufficient permissions to create knowledge base at '{base_directory}': {e}")
    except OSError as e:
        raise OSError(f"Failed to create knowledge base directory structure: {e}")


def _parse_hierarchical_structure(structure_list: List[str]) -> List[str]:
    """
    Parse hierarchical structure and convert to directory paths.
    
    Args:
        structure_list: List of numbered hierarchical items (e.g., "2.1. Title")
        
    Returns:
        List of directory paths representing the hierarchy
    """
    directory_paths = []
    section_map = {}  # Map section numbers to their titles
    
    for item in structure_list:
        # Extract section number and title
        parts = item.split('. ', 1)
        if len(parts) != 2:
            continue
            
        section_num = parts[0]
        title = parts[1]
        
        # Store the mapping
        section_map[section_num] = title
        
        # Build the directory path based on the hierarchy
        levels = section_num.split('.')
        path_components = []
        
        # Build path by looking up each level in the hierarchy
        for i in range(len(levels)):
            current_section = '.'.join(levels[:i+1])
            if current_section in section_map:
                path_components.append(section_map[current_section])
        
        # Create directory path from path components
        if path_components:
            dir_path = '/'.join(path_components)
            directory_paths.append(dir_path)
    
    return directory_paths


def create_sample_or_content(base_directory: str) -> str:
    """
    Create sample content files in the Operations Research knowledge base.
    
    This creates placeholder README files in key directories to demonstrate
    the structure and provide templates for knowledge entry.
    
    Args:
        base_directory (str): Path to the existing OR knowledge base
        
    Returns:
        str: Success message with count of files created
    """
    
    sample_content = {
        "Operations Research/README.md": """# Operations Research Knowledge Base

This knowledge base contains comprehensive information about Operations Research theory, methods, and applications.

## Structure

- **Modeling approaches**: Different ways to formulate OR problems
- **Heuristic versus optimization procedures**: Comparison of solution methodologies

## Usage

Each subdirectory contains specific knowledge about OR topics including:
- Theoretical foundations
- Mathematical formulations  
- Solution algorithms
- Practical applications
- Implementation examples
""",
        
        "Linear Programming (LP)/README.md": """# Linear Programming

Linear Programming is a mathematical optimization technique for solving problems with linear constraints and objectives.

## Key Concepts

- **Objective function**: Linear function to maximize or minimize
- **Constraints**: Linear inequalities or equalities  
- **Feasible region**: Set of points satisfying all constraints
- **Optimal solution**: Best solution within feasible region

## Topics Covered

- Applications (diet, scheduling, budgeting, blending)
- Modeling techniques and assumptions
- Solution methods (simplex, interior-point)
- Advanced topics (duality, sensitivity analysis)
""",
        
        "Integer Programming/README.md": """# Integer Programming

Integer Programming extends linear programming by requiring some or all variables to take integer values.

## Applications

- Capital budgeting decisions
- Set covering and partitioning
- Fixed-charge problems
- Logical constraints (either-or, if-then)

## Solution Methods

- Branch-and-bound algorithm
- Cutting plane methods
- Specialized algorithms (TSP solutions)
""",
        
        "Metaheuristics/README.md": """# Metaheuristics

Metaheuristics are high-level problem-independent algorithmic frameworks for solving complex optimization problems.

## Techniques Covered

- **Local search**: Greedy, steepest ascent/descent
- **Population-based**: Genetic algorithms, particle swarm
- **Trajectory-based**: Tabu search, simulated annealing
- **Nature-inspired**: Ant colony optimization

## Applications

These methods are particularly useful for NP-hard problems where exact methods are computationally intractable.
"""
    }
    
    try:
        base_path = Path(base_directory)
        if not base_path.exists():
            raise FileNotFoundError(f"Knowledge base directory '{base_directory}' does not exist")
            
        files_created = 0
        for file_path, content in sample_content.items():
            full_path = base_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            files_created += 1
            
        return f"Created {files_created} sample content files in the OR knowledge base"
        
    except Exception as e:
        raise Exception(f"Failed to create sample content: {e}")


if __name__ == "__main__":
    # Example usage
    kb_path = "or_knowledge_base_example"
    
    try:
        # Create the knowledge base structure
        result = create_or_knowledge_base(kb_path)
        print(result)
        
        # Add sample content
        content_result = create_sample_or_content(kb_path)
        print(content_result)
        
        print(f"\nKnowledge base created successfully at: {os.path.abspath(kb_path)}")
        
    except Exception as e:
        print(f"Error: {e}") 