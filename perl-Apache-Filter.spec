# it wants a module from mod_perl-1.x
%define _requires_exceptions perl(Apache::RegistryNG)

%define realname Apache-Filter

Summary:	%{realname} module for perl
Name:		perl-%{realname}
Version:	1.024
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{realname}-%{version}.tar.bz2
Patch0:		Apache-Filter-1.024-mod_perl2.diff
Requires:	apache-mod_perl
BuildRequires:	apache-mod_perl 
BuildRequires:  perl-devel
#BuildRequires:	perl-Apache-Test
BuildArch:	noarch

%description
%{realname} module for perl : Alter the output of previous handlers.

%prep

%setup -q -n %{realname}-%{version}
%patch0 -p0

%build
APACHE=%{_sbindir}/httpd perl Makefile.PL INSTALLDIRS=vendor <<EOF


EOF
make

#make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}

%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Apache
%{_mandir}/*/*



