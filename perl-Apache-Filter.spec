%define upstream_name    Apache-Filter
%define upstream_version 1.024

# it wants a module from mod_perl-1.x
%define _requires_exceptions perl(Apache::RegistryNG)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Apache-Filter-1.024-mod_perl2.diff

BuildRequires:	apache-mod_perl 
BuildRequires:  perl-devel

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	apache-mod_perl

%description
%{upstream_name} module for perl : Alter the output of previous handlers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
APACHE=%{_sbindir}/httpd perl Makefile.PL INSTALLDIRS=vendor <<EOF


EOF
%make

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
