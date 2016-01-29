#
%include        /usr/lib/rpm/macros.mono
#
Summary:	A profiler to explore live objects in the heap
Summary(pl.UTF-8):	Profiler do podglądania żywych obiektów na stercie
Name:		heap-shot
Version:	0.2
%define	snap	20151022
%define	gitref	84033f7b9c19972b761ad0203c391b70fcf9c1a7
%define	rel	1
Release:	0.%{gitref}.%{rel}
License:	GPL v3
Group:		Development/Tools
Source0:	https://github.com/mono/heap-shot/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	57a49b9f83d3d5cb079b5d710398719e
Patch0:		%{name}-wrapper.patch
URL:		http://www.mono-project.com/HeapShot
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2
BuildRequires:	mono-csharp >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap Shot is a profiler to explore memory allocation patterns in an
application is it part of the Mono profiling tools. Heap Shot works by
taking snapshots of the Mono managed heap from running Mono
applications and displaying the results. Additionally, Heap Shot can
compare the differences in live objects between a number of snapshots,
this is very helpful to understand which objects are alive and which
objects have been allocated. Heap Shot can either explore one snapshot
of memory at a point, or it can be used to compare the objects between
two separate points in time.

%description -l pl.UTF-8
Heap Shot to profiler do obserwacji wzorców przydzielania pamięci w
aplikacji. Jest częścią narzędzi profilujących Mono. Działa poprzez
wykonywanie migawek sterty zarządzanej przez Mono z działających
aplikacji Mono oraz wyświetlanie wyników. Dodatkowo Heap Shot potrafi
porównywać różnice w żywych obiektach między wieloma migawkami, co
jest bardzo pomocne dla zrozumienia, które obiekty zostały powołane do
życia, a które przydzielone. Heap Shot pozwala przeglądać pojedynczą
migawkę pamięci z jakiejś chwili, albo porównywać obiekty między
dwiema różnymi chwilami.

%prep
%setup -q -n %{name}-%{gitref}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/heap-shot-gui
%{_prefix}/lib/%{name}
