Name:           python-thrift
Version:        0.9.1
Release:        1
Summary:        Thrift Python Software Library

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/thrift
Source0:        http://pypi.python.org/packages/source/t/thrift/thrift-%{version}.tar.gz

BuildRequires:  python-devel

%description
Thrift Python Software Library

Thrift is provided as a set of Python packages. The top level package is
thrift, and there are subpackages for the protocol, transport, and server
code. Each package contains modules using standard Thrift naming conventions
(i.e. TProtocol, TTransport) and implementations in corresponding modules
(i.e. TSocket).  There is also a subpackage reflection, which contains
the generated code for the reflection structures.

%prep
%setup -q -n thrift-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{python_sitearch}/*

%changelog
* Fri Sep 6 2013 Dan Prince - 0.9.1-1
- Initial package.
