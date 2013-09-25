%define upstream_name    CPAN-Checksums
%define upstream_version 2.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Write a C<CHECKSUMS> file for a directory as on CPAN
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/CPAN-Checksums-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Bzip2)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Data::Compare)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(DirHandle)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)

BuildArch:	noarch

%description
* $success = updatedir($dir)

  'updatedir()' takes a directory name as argument and writes a typical
  'CHECKSUMS' file in that directory as used on CPAN unless a previously
  written 'CHECKSUMS' file is there that is still valid. Returns 2 if a new
  'CHECKSUMS' file has been written, 1 if a valid 'CHECKSUMS' file is
  already there, otherwise dies.

  Note: since version 2.0 updatedir on empty directories behaves just the
  same. In older versions it silently did nothing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f *.list
rm -f t/00signature.t
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.70.0-2mdv2011.0
+ Revision: 656883
- rebuild for updated spec-helper

* Sun Nov 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.70.0-1mdv2011.0
+ Revision: 599549
- update to new version 2.07

* Sun Nov 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.60.0-1mdv2011.0
+ Revision: 597485
- remove signature tests
- update to 2.06

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2011.0
+ Revision: 495425
- update to 2.05

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.1
+ Revision: 482125
- import perl-CPAN-Checksums


* Thu Dec 24 2009 cpan2dist 2.04-1mdv
- initial mdv release, generated with cpan2dist

