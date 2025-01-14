from pathlib import Path
from typing import Optional


class JobExecutorConfig(object):
    """An abstract configuration class for :class:`~psij.JobExecutor` instances."""

    DEFAULT: 'JobExecutorConfig' = None  # type: ignore

    DEFAULT_WORK_DIRECTORY = Path.home() / '.psij' / 'work'

    def __init__(self, launcher_log_file: Optional[Path] = None,
                 work_directory: Optional[Path] = None) -> None:
        """
        Initializes a configuration object.

        Parameters
        ----------
        launcher_log_file
            If specified, log messages from launcher scripts (including
            output from pre- and post- launch scripts) will be directed to this file.
        work_directory
            A directory where submit scripts and auxiliary job files will be generated. In a,
            cluster this directory needs to point to a directory on a shared filesystem. This is so
            that the exit code file, likely written on a service node, can be accessed by PSI/J,
            likely running on a head node.
        """
        self.launcher_log_file = launcher_log_file
        if work_directory:
            self.work_directory = work_directory
        else:
            self.work_directory = JobExecutorConfig.DEFAULT_WORK_DIRECTORY


JobExecutorConfig.DEFAULT = JobExecutorConfig()
