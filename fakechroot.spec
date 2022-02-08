Name:           fakechroot
Version:        2.20.1
Release:        1
Summary:        Gives a fake chroot environment
License:        LGPLv2+
URL:            https://github.com/dex4er/fakechroot
Source0:        https://github.com/dex4er/fakechroot/archive/%{version}/fakechroot-%{version}.tar.gz

#Patch1 URL:         https://github.com/dex4er/fakechroot/commit/b42d1fb9538f680af2f31e864c555414ccba842a.patch
#Patch2 URL:         https://github.com/dex4er/fakechroot/pull/85/commits/534e6d555736b97211523970d378dfb0db2608e9.patch
#Patch3 URL:         https://github.com/dex4er/fakechroot/pull/85/commits/75d7e6fa191c11a791faff06a0de86eaa7801d05.patch
#Patch4 URL:         https://github.com/dex4er/fakechroot/pull/85/commits/693a3597ea7fccfb62f357503ff177bd3e3d5a89.patch
#Patch5 URL:         https://github.com/dex4er/fakechroot/pull/86.patch
Patch1:         b42d1fb9538f680af2f31e864c555414ccba842a.patch
Patch2:         534e6d555736b97211523970d378dfb0db2608e9.patch
Patch3:         75d7e6fa191c11a791faff06a0de86eaa7801d05.patch
Patch4:         693a3597ea7fccfb62f357503ff177bd3e3d5a89.patch
Patch5:         86.patch


Requires:       binutils binutils-devel
Provides:       fakechroot-libs = %{version}-%{release}
Obsoletes:      fakechroot-libs < %{version}-%{release}
BuildRequires:  autoconf automake libtool perl-podlators perl-generators
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gdbm-libs
Requires:       /usr/bin/objdump

%description
fakechroot creates a fake environment in which user could run a command and
use the chroot(8) call without root privileges. This is useful when user want
a chrooted environment to install other packages without elevating privileges.

%package        help
Summary:        Documentation of fakechroot
%description    help
The documentation of fakechroot.

%prep
%autosetup -p1
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%build
autoreconf -vfi
%configure --disable-static --disable-silent-rules --with-libpath="%{_libdir}/fakechroot:/usr/lib/fakechroot"
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%check
%make_build check

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%license COPYING LICENSE
%{_bindir}/*fakechroot
%{_sbindir}/chroot.fakechroot
%config(noreplace) %{_sysconfdir}/fakechroot/*.env
%{_libdir}/fakechroot/

%files          help
%doc NEWS.md README.md THANKS.md
%{_mandir}/man1/fakechroot.1*

%changelog
* Tue Jan 18 2022 SimpleUpdate Robot <tc@openeuler.org> - 2.20.1-1
- Upgrade to version 2.20.1

* Wed Jun 30 2021 caodongxia<caodongxia@huawei.com> - 2.19-9
- Fix '_STAT_VER' undeclared

* Wed Jan 22 2020 gulining<gulining1@huawei.com> - 2.19-8
- Disable test

* Wed Nov 27 2019 lihao <lihao129@huawei.com> - 2.19-7
- Package Init

