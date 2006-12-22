#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Raw-Bzip2
Summary:	Compress::Raw::Bzip2 - Low-Level Interface to bzip2 compression library
Summary(pl):	Niskopoziomowy interfejs do biblioteki kompresji bzip2
Name:		perl-Compress-Raw-Bzip2
Version:	2.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d153d4c3eadf6d68c75f78dcc427cff
Patch0:		%{name}-system-bzip2.patch
URL:		http://search.cpan.org/dist/Compress-Raw-Bzip2/
BuildRequires:	bzip2-devel >= 1.0.3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::Raw::Bzip2 provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression
library.

Although the primary purpose for the existence of Compress::Raw::Bzip2
is for use by the IO::Compress::Bzip2 and IO::Uncompress::Bunzip2
modules, it can be used on its own for simple
compression/uncompression tasks.

%description -l pl
Compress::Raw::Bzip2 udostêpnia interfejs do funkcji
kompresji/dekompresji w pamiêci z biblioteki kompresji bzip2.

Choæ g³ównym celem istnienia Compress::Raw::Bzip2 jest wykorzystywanie
przez modu³y IO::Compress::Bzip2 i IO::Uncompress::Bunzip2, mo¿na tego
modu³u u¿yæ samodzielnie do prostych zadañ kompresji/dekompresji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Compress/Raw/Bzip2.pm
%dir %{perl_vendorarch}/auto/Compress/Raw/Bzip2
%{perl_vendorarch}/auto/Compress/Raw/Bzip2/Bzip2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Raw/Bzip2/Bzip2.so
%{perl_vendorarch}/auto/Compress/Raw/Bzip2/autosplit.ix
%{_mandir}/man3/Compress::Raw::Bzip2.3*
