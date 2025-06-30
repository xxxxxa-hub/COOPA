#!/usr/bin/env python3
"""
Accuracy Analyzer for Experiment Results

This script analyzes the accuracy of experiment results by comparing predicted answers
to gold standard answers using a configurable threshold.

Usage:
    python accuracy_analyzer.py <file_path> <threshold>

Example:
    python accuracy_analyzer.py datasets/nlp4opt/experiment_results_20250630_005435.jsonl 1e-4
"""

import json
import argparse
import sys
from pathlib import Path


def analyze_accuracy(file_path, threshold):
    """
    Analyze the accuracy of predictions in a JSONL file.
    
    Args:
        file_path (str): Path to the JSONL file containing experiment results
        threshold (float): Threshold for considering a prediction correct
        
    Returns:
        dict: Dictionary containing accuracy statistics
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    total_problems = 0
    correct_predictions = 0
    errors = []
    detailed_results = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                    
                try:
                    data = json.loads(line)
                    
                    # Extract required fields
                    index = data.get('index', line_num)
                    gold_answer = data.get('gold_answer')
                    predicted_answer = data.get('predicted_answer')
                    
                    # Skip if any required field is missing or None
                    if gold_answer is None or predicted_answer is None:
                        errors.append(f"Line {line_num}: Missing gold_answer or predicted_answer")
                        continue
                    
                    # Convert to float for comparison
                    try:
                        gold_float = float(gold_answer)
                        pred_float = float(predicted_answer)
                    except (ValueError, TypeError):
                        errors.append(f"Line {line_num}: Could not convert answers to float - gold: {gold_answer}, predicted: {predicted_answer}")
                        continue
                    
                    # Calculate absolute difference
                    abs_diff = abs(gold_float - pred_float)
                    is_correct = abs_diff < threshold
                    
                    total_problems += 1
                    if is_correct:
                        correct_predictions += 1
                    
                    detailed_results.append({
                        'index': index,
                        'gold_answer': gold_float,
                        'predicted_answer': pred_float,
                        'absolute_difference': abs_diff,
                        'is_correct': is_correct
                    })
                    
                except json.JSONDecodeError as e:
                    errors.append(f"Line {line_num}: JSON decode error - {e}")
                    continue
                    
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {e}")
    
    # Calculate accuracy
    accuracy = correct_predictions / total_problems if total_problems > 0 else 0.0
    
    return {
        'file_path': file_path,
        'threshold': threshold,
        'total_problems': total_problems,
        'correct_predictions': correct_predictions,
        'incorrect_predictions': total_problems - correct_predictions,
        'accuracy': accuracy,
        'accuracy_percentage': accuracy * 100,
        'errors': errors,
        'detailed_results': detailed_results
    }


def print_summary(results):
    """Print a summary of the accuracy analysis."""
    print("=" * 60)
    print("ACCURACY ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"File: {results['file_path']}")
    print(f"Threshold: {results['threshold']}")
    print("-" * 60)
    print(f"Total Problems: {results['total_problems']}")
    print(f"Correct Predictions: {results['correct_predictions']}")
    print(f"Incorrect Predictions: {results['incorrect_predictions']}")
    print(f"Accuracy: {results['accuracy']:.6f} ({results['accuracy_percentage']:.2f}%)")
    
    if results['errors']:
        print(f"\nErrors encountered: {len(results['errors'])}")
        print("First 5 errors:")
        for error in results['errors'][:5]:
            print(f"  - {error}")
        if len(results['errors']) > 5:
            print(f"  ... and {len(results['errors']) - 5} more errors")
    
    print("=" * 60)


def print_detailed_results(results, max_examples=10):
    """Print detailed results for some examples."""
    print(f"\nDETAILED RESULTS (showing first {max_examples} examples)")
    print("-" * 80)
    print(f"{'Index':<6} {'Gold':<12} {'Predicted':<12} {'Abs Diff':<12} {'Correct':<8}")
    print("-" * 80)
    
    for i, result in enumerate(results['detailed_results'][:max_examples]):
        print(f"{result['index']:<6} "
              f"{result['gold_answer']:<12.4f} "
              f"{result['predicted_answer']:<12.4f} "
              f"{result['absolute_difference']:<12.6f} "
              f"{'✓' if result['is_correct'] else '✗':<8}")
    
    if len(results['detailed_results']) > max_examples:
        print(f"... and {len(results['detailed_results']) - max_examples} more results")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze accuracy of experiment results with configurable threshold",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python accuracy_analyzer.py datasets/nlp4opt/experiment_results_20250630_005435.jsonl 1e-4
  python accuracy_analyzer.py datasets/nlp4opt/experiment_results_20250630_005435.jsonl 0.01
  python accuracy_analyzer.py datasets/nlp4opt/experiment_results_20250630_005435.jsonl 1.0
        """
    )
    
    parser.add_argument('--file_path', type=str, help='Path to the JSONL file containing experiment results')
    parser.add_argument('--threshold', type=float, help='Threshold for considering a prediction correct')
    parser.add_argument('--detailed', '-d', action='store_true', help='Show detailed results for individual problems')
    parser.add_argument('--max-examples', type=int, default=10, help='Maximum number of detailed examples to show')
    
    args = parser.parse_args()
    
    try:
        # Analyze accuracy
        results = analyze_accuracy(args.file_path, args.threshold)
        
        # Print summary
        print_summary(results)
        
        # Print detailed results if requested
        if args.detailed:
            print_detailed_results(results, args.max_examples)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 