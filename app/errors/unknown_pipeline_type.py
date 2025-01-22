class UnknownPipelineType(Exception):
    def __init__(self, pipeline_type: str):
        self.message = f"Pipeline type '{pipeline_type}' does not exist."
        super().__init__(self.message)
