import yaml


class JobHelper:
    def __init__(self, config_file: str = "metadata.yaml"):
        self._config_file = config_file
        self._ensure_config_file_exists()

    def _ensure_config_file_exists(self) -> None:
        try:
            with open(self._config_file, "r") as file:
                yaml.safe_load(file)
        except FileNotFoundError:
            with open(self._config_file, "w") as file:
                yaml.safe_dump({"job": {"job_id": 0}}, file)

    def get_job_id(self) -> int:
        try:
            with open(self._config_file, "r") as file:
                config = yaml.safe_load(file)
                job_id = config.get("job", {}).get("job_id", 0)

            new_job_id = job_id + 1

            self._update_job_id(new_job_id)

            return new_job_id

        except FileNotFoundError:
            self._update_job_id(1)
            return 1
        except KeyError:
            raise ValueError("job_id is missing in the configuration")

    def _update_job_id(self, new_job_id: int) -> None:
        try:
            with open(self._config_file, "r") as file:
                config = yaml.safe_load(file)

            if "job" not in config:
                config["job"] = {}

            config["job"]["job_id"] = new_job_id

            with open(self._config_file, "w") as file:
                yaml.safe_dump(config, file)

        except FileNotFoundError:
            config = {"job": {"job_id": new_job_id}}
            with open(self._config_file, "w") as file:
                yaml.safe_dump(config, file)
