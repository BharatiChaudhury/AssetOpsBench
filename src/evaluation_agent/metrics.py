import time
from typing import Any, Dict, List, Optional

class MetricsEvaluator:
    def __init__(self):
        self.metrics = {}
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()
        self.metrics['response_time'] = self.end_time - self.start_time

    def record_task_completion(self, success: bool):
        self.metrics['task_completed'] = success

    def record_accuracy(self, correct: bool):
        self.metrics['accuracy'] = correct

    def record_partial_score(self, score: float):
        self.metrics['partial_score'] = score

    def record_num_steps(self, steps: int):
        self.metrics['num_steps'] = steps

    def record_resource_utilization(self, cpu: float = None, memory: float = None):
        if cpu is not None:
            self.metrics['cpu_usage'] = cpu
        if memory is not None:
            self.metrics['memory_usage'] = memory

    def record_reasoning_quality(self, score: float):
        self.metrics['reasoning_quality'] = score

    def record_hallucination(self, hallucinated: bool):
        self.metrics['hallucination'] = hallucinated

    def record_consistency(self, consistent: bool):
        self.metrics['consistency'] = consistent

    def record_robustness(self, robust: bool):
        self.metrics['robustness'] = robust

    def record_generalization(self, generalized: bool):
        self.metrics['generalization'] = generalized

    def record_agent_selection(self, correct: bool):
        self.metrics['correct_agent_invocation'] = correct

    def record_inter_agent_communication(self, quality: float):
        self.metrics['inter_agent_communication_quality'] = quality

    def record_workflow_optimality(self, optimal: bool):
        self.metrics['workflow_optimality'] = optimal

    def record_output_clarity(self, clarity: float):
        self.metrics['output_clarity'] = clarity

    def record_justification_quality(self, quality: float):
        self.metrics['justification_quality'] = quality

    def record_user_satisfaction(self, score: float):
        self.metrics['user_satisfaction'] = score

    def record_self_verification(self, verified: bool):
        self.metrics['self_verification'] = verified

    def record_external_verification(self, verified: bool):
        self.metrics['external_verification'] = verified

    def record_failure_mode_coverage(self, num_modes: int):
        self.metrics['failure_mode_coverage'] = num_modes

    def record_recovery_from_failure(self, recovered: bool):
        self.metrics['recovery_from_failure'] = recovered

    def record_traceability(self, traceable: bool):
        self.metrics['traceability'] = traceable

    def record_action_reason_alignment(self, aligned: bool):
        self.metrics['action_reason_alignment'] = aligned

    def record_throughput(self, throughput: float):
        self.metrics['throughput'] = throughput

    def record_performance_degradation(self, degraded: bool):
        self.metrics['performance_degradation'] = degraded

    def get_metrics(self) -> Dict[str, Any]:
        return self.metrics

    def reset(self):
        self.metrics = {}
        self.start_time = None
        self.end_time = None 