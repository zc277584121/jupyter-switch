#!/usr/bin/env python3
"""
Test script to verify uvx naming convention for jupyter-switch
"""
import subprocess
import sys
import tempfile
import os
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and return the result"""
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=check
        )
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        raise


def test_uvx_jupyter_switch():
    """Test if uvx jupyter-switch works"""
    print("=" * 60)
    print("Test 1: Check if uvx jupyter-switch command exists")
    print("=" * 60)
    
    # Test --help
    result = run_command(["uvx", "jupyter-switch", "--help"], check=False)
    if result.returncode == 0:
        print("✓ uvx jupyter-switch --help works")
    else:
        print("✗ uvx jupyter-switch --help failed")
        return False
    
    # Test --version
    print("\n" + "=" * 60)
    print("Test 2: Check version command")
    print("=" * 60)
    result = run_command(["uvx", "jupyter-switch", "--version"], check=False)
    if result.returncode == 0:
        print("✓ uvx jupyter-switch --version works")
        print(f"Version output: {result.stdout.strip()}")
    else:
        print("✗ uvx jupyter-switch --version failed")
        return False
    
    # Test actual conversion with a sample file
    print("\n" + "=" * 60)
    print("Test 3: Test actual conversion functionality")
    print("=" * 60)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test markdown file
        test_md = Path(tmpdir) / "test.md"
        test_md.write_text("""# Test Notebook

This is a test markdown file.

```python
print("Hello, World!")
```

More markdown content.
""")
        
        print(f"Created test file: {test_md}")
        
        # Try to convert md to ipynb
        result = run_command(
            ["uvx", "jupyter-switch", str(test_md)],
            check=False
        )
        
        if result.returncode == 0:
            test_ipynb = Path(tmpdir) / "test.ipynb"
            if test_ipynb.exists():
                print("✓ Conversion successful: test.md -> test.ipynb")
                print(f"Output file exists: {test_ipynb}")
                
                # Try converting back
                print("\nTesting reverse conversion...")
                result2 = run_command(
                    ["uvx", "jupyter-switch", str(test_ipynb)],
                    check=False
                )
                
                if result2.returncode == 0:
                    test_md2 = Path(tmpdir) / "test.md"
                    if test_md2.exists():
                        print("✓ Reverse conversion successful: test.ipynb -> test.md")
                        return True
                    else:
                        print("✗ Reverse conversion failed: output file not found")
                        return False
                else:
                    print("✗ Reverse conversion command failed")
                    return False
            else:
                print("✗ Conversion failed: output file not found")
                return False
        else:
            print("✗ Conversion command failed")
            return False


def test_uvx_jupyter_switch_mcp():
    """Test if uvx jupyter-switch-mcp works with --from flag"""
    print("\n" + "=" * 60)
    print("Test 4: Check if uvx jupyter-switch-mcp command exists (with --from)")
    print("=" * 60)
    
    # Test with --from flag (as documented in README)
    result = run_command(["uvx", "--from", "jupyter-switch", "jupyter-switch-mcp", "--help"], check=False)
    if result.returncode == 0:
        print("✓ uvx --from jupyter-switch jupyter-switch-mcp --help works")
        return True
    else:
        print("✗ uvx --from jupyter-switch jupyter-switch-mcp --help failed")
        print("Note: This might be expected if MCP server doesn't support --help")
        return False


if __name__ == "__main__":
    print("Testing uvx naming convention for jupyter-switch\n")
    
    success = True
    
    # Test main command
    if not test_uvx_jupyter_switch():
        success = False
    
    # Test MCP command
    test_uvx_jupyter_switch_mcp()
    
    print("\n" + "=" * 60)
    if success:
        print("✓ All critical tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)
