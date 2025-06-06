import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging
from typing import List, Dict, Tuple
import random
import warnings
try:
    from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
    import torch
except ImportError:
    warnings.warn("Transformers library not found. Using mock model for demo.")
    transformers_available = False
else:
    transformers_available = True

# Configure logging for test results
logging.basicConfig(filename='validation_report.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MockVoiceClassifier:
    """Mock classifier for environments without transformers."""
    def __init__(self):
        self.commands = ["play music", "navigate to", "call contact", "stop"]
        self.accuracy = 0.95
    
    def predict(self, audio_input: str) -> Tuple[str, float]:
        if random.random() < self.accuracy:
            for cmd in self.commands:
                if cmd in audio_input.lower():
                    return cmd, 0.9
        return "unknown", 0.1

class RealVoiceClassifier:
    """Real speech recognition model using Wav2Vec2."""
    def __init__(self):
        self.model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
        self.processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
        self.commands = ["play music", "navigate to", "call contact", "stop"]
    
    def predict(self, audio_input: str) -> Tuple[str, float]:
        # Simulate audio processing (in real scenario, use audio waveform)
        inputs = self.processor(audio_input, sampling_rate=16000, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = self.model(inputs.input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)[0].lower()
        
        for cmd in self.commands:
            if cmd in transcription:
                return cmd, 0.9
        return "unknown", 0.1

class AIVoiceValidation:
    """Enhanced validation pipeline for voice command recognition."""
    def __init__(self, use_real_model: bool = transformers_available):
        self.use_real_model = use_real_model
        self.model = RealVoiceClassifier() if use_real_model else MockVoiceClassifier()
        self.test_results = []
    
    def define_test_cases(self) -> List[Dict]:
        """Define extended test cases for diverse scenarios."""
        test_cases = [
            {"id": 1, "input": "play music", "expected": "play music", "condition": "clear English input"},
            {"id": 2, "input": "navigate to office", "expected": "navigate to", "condition": "valid English command"},
            {"id": 3, "input": "play music in noise", "expected": "play music", "condition": "noisy English input"},
            {"id": 4, "input": "invalid command", "expected": "unknown", "condition": "invalid English input"},
            {"id": 5, "input": "call contact now", "expected": "call contact", "condition": "extended English input"},
            {"id": 6, "input": "spiele musik", "expected": "play music", "condition": "clear German input"},
            {"id": 7, "input": "navegar a casa", "expected": "navigate to", "condition": "clear Spanish input"},
            {"id": 8, "input": "play music with accent", "expected": "play music", "condition": "accented English input"},
            {"id": 9, "input": "low quality stop", "expected": "stop", "condition": "low-quality audio input"}
        ]
        return test_cases
    
    def simulate_audio_input(self, text: str) -> str:
        """Simulate audio input processing (mock for demo purposes)."""
        # In a real scenario, process audio files or microphone input at 16kHz
        return text
    
    def run_validation(self, test_cases: List[Dict]) -> None:
        """Execute test cases and store results."""
        for test in test_cases:
            test_id = test["id"]
            input_text = self.simulate_audio_input(test["input"])
            predicted_cmd, confidence = self.model.predict(input_text)
            expected_cmd = test["expected"]
            condition = test["condition"]
            
            passed = predicted_cmd == expected_cmd
            result = {
                "test_id": test_id,
                "input": input_text,
                "expected": expected_cmd,
                "predicted": predicted_cmd,
                "confidence": confidence,
                "condition": condition,
                "passed": passed
            }
            self.test_results.append(result)
            logging.info(f"Test ID {test_id}: Condition={condition}, Passed={passed}, "
                        f"Input={input_text}, Predicted={predicted_cmd}, Confidence={confidence}")
    
    def generate_report(self) -> pd.DataFrame:
        """Generate a summary report of test results."""
        df = pd.DataFrame(self.test_results)
        pass_rate = df["passed"].mean() * 100
        report_summary = f"Validation Report - {datetime.now()}\n"
        report_summary += f"Total Tests: {len(df)}\n"
        report_summary += f"Pass Rate: {pass_rate:.2f}%\n"
        report_summary += f"Failed Tests: {len(df[~df['passed']])}\n"
        report_summary += f"Model Used: {'Real (Wav2Vec2)' if self.use_real_model else 'Mock'}\n"
        
        logging.info(report_summary)
        print(report_summary)
        return df
    
    def visualize_results(self, filename: str = "validation_results.png") -> None:
        """Visualize test results using matplotlib."""
        df = pd.DataFrame(self.test_results)
        pass_counts = df["passed"].value_counts()
        labels = ["Passed", "Failed"] if len(pass_counts) == 2 else ["Passed"] if pass_counts.get(True, 0) else ["Failed"]
        counts = [pass_counts.get(True, 0), pass_counts.get(False, 0)]
        
        plt.figure(figsize=(6, 4))
        plt.bar(labels, counts, color=["green", "red"])
        plt.title("Test Case Pass/Fail Distribution")
        plt.ylabel("Number of Tests")
        plt.savefig(filename)
        plt.close()
        logging.info(f"Visualization saved to {filename}")
    
    def save_report(self, filename: str = "validation_report.csv") -> None:
        """Save test results to a CSV file."""
        df = self.generate_report()
        df.to_csv(filename, index=False)
        logging.info(f"Report saved to {filename}")
        self.visualize_results()

def main():
    """Run the enhanced AI validation pipeline."""
    validator = AIVoiceValidation(use_real_model=transformers_available)
    test_cases = validator.define_test_cases()
    validator.run_validation(test_cases)
    validator.save_report()

if __name__ == "__main__":
    main()