%define cvsversion 20061128
Name: glean
Version: 1.1
Release: %mkrel 2.cvs%{cvsversion}
Summary: A suite of tools for evaluating the quality of an OpenGL implementation 
Group: System/X11
URL: http://glean.sourceforge.net
# CVS snapshot
# cvs -z3 -d:pserver:anonymous@glean.cvs.sourceforge.net:/cvsroot/glean co -d glean-$(date +%Y%m%d) glean
# tar jcf glean-$(date +%Y%m%d).tar.bz2 glean-$(date +%Y%m%d)
Source: glean-%{cvsversion}.tar.bz2
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com> 
BuildRoot: %{_tmppath}/%{name}-root

%if %mdkversion >= 200700
BuildRequires: GL-devel
BuildRequires: libmesaglu-devel
BuildRequires: libmesaglut-devel
%else
BuildRequires: libxorg-x11-devel
BuildRequires: libMesaGLU-devel
BuildRequires: libMesaglut-devel
%endif
BuildRequires: libtiff-devel

%description
Glean is a suite of tools for evaluating the quality of an OpenGL
implementation and diagnosing any problems that are discovered. glean also
has the ability to compare two OpenGL implementations and highlight the
differences between them.

Who should care about glean? 
 - Anyone who buys or reviews graphics cards. glean gives you the ability to 
   compare performance, features, and image quality of different graphics cards. 
   Since the source code is freely available, you can customize glean to add 
   tests for the things that are most important to you. 

 - Software developers. With glean you can learn which features really work for 
   a given combination of hardware and driver. You can also find the timing for 
   basic drawing operations, mode changes, texture downloads, etc. so that you 
   can maximize the performance of your application. 

 - OpenGL driver developers. glean can increase your confidence that your driver 
   software is correct and efficient. It also allows you to compare a new release 
   to a previous release, to make sure that there are no regressions in quality 
   or performance.

%prep
%setup -q -n %{name}-%{cvsversion}

%build
GLEAN_ROOT=`pwd`
export GLEAN_ROOT

# (boiko) glean uses a different way for compiling its sources, so we have to 
#         use make install here
pushd src
make install
popd

%install
rm -rf %{buildroot}
# We have to install everything by hand
mkdir -p %{buildroot}%{_bindir}

# install binaries
install -m0755 bin/difftiff %{buildroot}%{_bindir}/
install -m0755 bin/glean %{buildroot}%{_bindir}/
install -m0755 bin/showtiff %{buildroot}%{_bindir}/
install -m0755 bin/showvis %{buildroot}%{_bindir}/


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYRIGHT
%{_bindir}/difftiff
%{_bindir}/glean
%{_bindir}/showtiff
%{_bindir}/showvis


