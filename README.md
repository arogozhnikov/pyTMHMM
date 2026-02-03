## pytmhmm_binaries

this is a fork of pyTMHMM <https://github.com/bosborne/pyTMHMM> 

Things that were changed: minor updates for newer python versions / newer python packaging. 

To build multilinux/musllinux binaries for x86 and arm:

```bash
CIBW_ARCHS_LINUX="x86_64 aarch64" uvx cibuildwheel --platform linux
```

publishing to pypi:

```bash
# binary distribution
uv publish wheelhouse/*.whl
# source distribution
uv publish
```

