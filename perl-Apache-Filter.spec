%define upstream_name    Apache-Filter
%define upstream_version 1.024

# it wants a module from mod_perl-1.x
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Apache::RegistryNG\\)'
%else
%define _requires_exceptions perl(Apache::RegistryNG)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Apache-Filter-1.024-mod_perl2.diff

BuildRequires:	apache-mod_perl 
BuildRequires:	perl-devel

BuildArch:	noarch

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

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Apache
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.24.0-8mdv2011.0
+ Revision: 680452
- mass rebuild

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.24.0-7mdv2011.0
+ Revision: 504563
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.024-6mdv2010.0
+ Revision: 430257
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.024-5mdv2009.0
+ Revision: 241147
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.024-3mdv2007.0
+ Revision: 73195
- import perl-Apache-Filter-1.024-3mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.024-3mdk
- Fix SPEC Using perl Policies
	- Source URL

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 1.024-2mdk
- fix deps with P0 (fixes only mod_perl2 dependencies)
- filter out one mod_perl-1.x dep

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.024-1mdk
- New release 1.024

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.023-1mdk
- 1.023

* Tue Jun 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.022-3mdk
- Fix build with new httpd path

