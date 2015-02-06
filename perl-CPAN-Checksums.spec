%define upstream_name    CPAN-Checksums
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Write a C<CHECKSUMS> file for a directory as on CPAN

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

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


