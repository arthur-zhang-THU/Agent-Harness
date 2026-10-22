import subprocess
import sys
from pathlib import Path

import mini_swift


def test_mini_swift_module_and_public_exports():
    assert mini_swift.Swift is not None
    assert mini_swift.FakeModelClient is not None
    assert not hasattr(mini_swift, "MiniAgent")
    result = subprocess.run([sys.executable, "-m", "mini_swift", "--help"], capture_output=True, text=True, check=True)
    assert "Teaching-sized Swift agent harness" in result.stdout


def test_readme_main_mapping_points_to_existing_files():
    repo_root = Path(__file__).resolve().parents[3]
    main_files = [
        "swift/cli.py",
        "swift/runtime.py",
        "swift/agent_loop.py",
        "swift/context_manager.py",
        "swift/providers/clients.py",
        "swift/tool_executor.py",
        "swift/tools.py",
        "swift/task_state.py",
        "swift/run_store.py",
        "swift/workspace.py",
    ]
    for path in main_files:
        assert (repo_root / path).exists()
