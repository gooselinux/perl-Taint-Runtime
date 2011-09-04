Name:           perl-Taint-Runtime
Version:        0.03
Release:        9%{?dist}
Summary:        Runtime enable taint checking
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Taint-Runtime
Source0:        http://search.cpan.org/CPAN/authors/id/R/RH/RHANDOM/Taint-Runtime-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Test::More)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module enables runtime taint checking, for cases where the -T
switch on the commandline is not appropriate or viable. There are
a somewhat limited number of legitimate use cases where you should 
use this module instead of the -T switch. Unless you have a specific and
good reason for not using the -T option, you should use the -T option.

%prep
%setup -q -n Taint-Runtime-%{version}
chmod +x is_taint_bench.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/Taint/
%{perl_vendorarch}/Taint/
%{_mandir}/man3/*.3*

%changelog
* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-9
- add readme
- Related: rhbz#543948

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.03-5
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.03-4
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-3
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-2
- license tag fix, rebuild for ppc32

* Tue Jul 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-1.1
- BR: perl(Test::More)

* Thu Jul 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-1
- bump to 0.03

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-2
- bump for FC-6

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-1
- Initial package for Fedora Extras
