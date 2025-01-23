import yaml


class JobHelper:
    def __init__(self, config_file: str = "metadata.yaml"):
        self._config_file = config_file
        self._ensure_config_file_exists()

    def _ensure_config_file_exists(self) -> None:
        default_config = {"job": {"job_id": 0, "download_url": ""}}
        try:
            with open(self._config_file, "r") as file:
                yaml.safe_load(file)
        except FileNotFoundError:
            with open(self._config_file, "w") as file:
                yaml.safe_dump(default_config, file)

    def _read_config(self) -> dict:
        with open(self._config_file, "r") as file:
            return yaml.safe_load(file)

    def _write_config(self, config: dict) -> None:
        with open(self._config_file, "w") as file:
            yaml.safe_dump(config, file)

    def get_job_id(self) -> int:
        config = self._read_config()
        job_id = config.get("job", {}).get("job_id", 0)
        new_job_id = job_id + 1
        self._update_job_id(new_job_id)
        return new_job_id

    def _update_job_id(self, new_job_id: int) -> None:
        config = self._read_config()
        config.setdefault("job", {})["job_id"] = new_job_id
        self._write_config(config)

    def get_download_url(self) -> str:
        config = self._read_config()
        return config.get("job", {}).get("download_url", "")

    def set_download_url(self, download_url: str) -> None:
        config = self._read_config()
        config.setdefault("job", {})["download_url"] = download_url
        self._write_config(config)
