#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyproject_api
Version  : 1.5.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/23/6f/d02d1cab4a30998806687036e03ffecbf66e35df6bfab5a29f22ec61a075/pyproject_api-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/6f/d02d1cab4a30998806687036e03ffecbf66e35df6bfab5a29f22ec61a075/pyproject_api-1.5.1.tar.gz
Summary  : API to interact with the python pyproject.toml based projects
Group    : Development/Tools
License  : MIT
Requires: pypi-pyproject_api-license = %{version}-%{release}
Requires: pypi-pyproject_api-python = %{version}-%{release}
Requires: pypi-pyproject_api-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# [`pyproject-api`](https://pyproject-api.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/pyproject-api?style=flat-square)](https://pypi.org/project/pyproject-api/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/pyproject-api.svg)](https://pypi.org/project/pyproject-api/)
[![Downloads](https://pepy.tech/badge/pyproject-api/month)](https://pepy.tech/project/pyproject-api/month)
[![check](https://github.com/tox-dev/pyproject-api/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/pyproject-api/actions/workflows/check.yml)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/pyproject-api/badge/?version=latest)](https://pyproject-api.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-pyproject_api package.
Group: Default

%description license
license components for the pypi-pyproject_api package.


%package python
Summary: python components for the pypi-pyproject_api package.
Group: Default
Requires: pypi-pyproject_api-python3 = %{version}-%{release}

%description python
python components for the pypi-pyproject_api package.


%package python3
Summary: python3 components for the pypi-pyproject_api package.
Group: Default
Requires: python3-core
Provides: pypi(pyproject_api)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-pyproject_api package.


%prep
%setup -q -n pyproject_api-1.5.1
cd %{_builddir}/pyproject_api-1.5.1
pushd ..
cp -a pyproject_api-1.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678720887
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyproject_api
cp %{_builddir}/pyproject_api-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyproject_api/57b7b1ca99152770f11d8ffb65996badc6cd322f || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyproject_api/57b7b1ca99152770f11d8ffb65996badc6cd322f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
