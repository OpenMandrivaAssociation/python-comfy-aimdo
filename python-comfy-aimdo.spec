Name:		python-comfy-aimdo
Version:	0.5.6
Release:	1
Summary:	AI Model Dynamic Offloader used by ComfyUI
License:	GPL-3.0
Group:		Development/Python
URL:		https://github.com/Comfy-Org/comfy-aimdo
Source0:	https://github.com/Comfy-Org/comfy-aimdo/archive/refs/tags/v%{version}/comfy-aimdo-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)

# setuptools-scm needs a git tree; pin the tagged version
%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
Python bindings for ComfyUI's AIMDO allocator. The optional native
aimdo_rocm.so / aimdo.so is not built in this package; ComfyUI
falls back to its own VRAM management if the .so is absent.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/comfy_aimdo
%{py_sitedir}/comfy_aimdo-*.*-info
