#
%include        /usr/lib/rpm/macros.mono
#
Summary:	A profiler to explore live objects in the heap
Name:		heap-shot
Version:	0.1
Release:	4
License:	GPL v3
Group:		Development/Tools
# git clone http://github.com/mono/heap-shot.git
Source0:	%{name}.tar.bz2
# Source0-md5:	976f917b5703eb321b7acac42e6f9000
Patch0:		%{name}-unicode-dot.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-fix.patch
URL:		http://www.mono-project.com/HeapShot
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 2.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap Shot is a profiler to explore memory allocation patterns in an
application is it part of the Mono profiling tools. Heap Shot works by
taking snapshots of the Mono managed heap from running Mono
applications and displaying the results. Additionally, Heap Shot can
compare the differences in live objects between a number of snapshots,
this is very helpful to understand which objects are alive and which
objects have been allocated. HeapShot can either explore one snapshot
of memory at a point, or it can be used to compare the objects between
two separate points in time.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# mono dlopens profiler library by libmono-profiler-NAME.so
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/heap-shot
%attr(755,root,root) %{_bindir}/heap-shot-gui
%attr(755,root,root) %{_libdir}/libmono-profiler-heap-shot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmono-profiler-heap-shot.so.0
%attr(755,root,root) %{_libdir}/libmono-profiler-heap-shot.so
%{_prefix}/lib/%{name}
