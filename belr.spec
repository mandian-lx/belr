%define oname Belr
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Belledonne Communications' language recognition library
Name:		%{lname}
Version:	0.1.0
Release:	1
License:	GPLv3+
Group:		Communications
URL:		https://www.linphone.org/technical-corner/%{name}
Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.1.0-path.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(udev)

%description
Belledonne Communications' language recognition library.

It aims at parsing any input formatted according to a language defined
by an ABNF grammar, such as the protocols standardized at IETF.

It is based on finite state machine theory and heavily relies on recursivity
from an implementation standpoint.

%files
%{_bindir}/%{name}*
%doc COPYING

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Belledonne Communications' language recognition library
Group:		System/Libraries

%description -n	%{libname}
Belledonne Communications' language recognition library.

It aims at parsing any input formatted according to a language defined
by an ABNF grammar, such as the protocols standardized at IETF.

It is based on finite state machine theory and heavily relies on recursivity
from an implementation standpoint.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%doc COPYING

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers, libraries and docs for the %{oname} library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the %{oname} library.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
#%{_libdir}/pkgconfig/lib%{name}.pc
%{_datadir}/%{oname}/cmake/
#doc README
%doc NEWS
%doc AUTHORS
#doc ChangeLog
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

