#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Compress
%define	pnam	Raw-Bzip2
Summary:	Compress::Raw::Bzip2 - Low-Level Interface to bzip2 compression library
Summary(pl.UTF-8):	Niskopoziomowy interfejs do biblioteki kompresji bzip2
Name:		perl-Compress-Raw-Bzip2
Version:	2.093
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c2034a80cc6bd674c308e03f051a46b9
URL:		http://search.cpan.org/dist/Compress-Raw-Bzip2/
BuildRequires:	bzip2-devel >= 1.0.3
BuildRequires:	perl-ExtUtils-MakeMaker >= 5.16
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

%description -l pl.UTF-8
Compress::Raw::Bzip2 udostępnia interfejs do funkcji
kompresji/dekompresji w pamięci z biblioteki kompresji bzip2.

Choć głównym celem istnienia Compress::Raw::Bzip2 jest wykorzystywanie
przez moduły IO::Compress::Bzip2 i IO::Uncompress::Bunzip2, można tego
modułu użyć samodzielnie do prostych zadań kompresji/dekompresji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Raw/Bzip2/Bzip2.so
%{_mandir}/man3/Compress::Raw::Bzip2.3pm*
