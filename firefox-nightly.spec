AutoReqProv: no

%define debug_package %{nil}
%global _optdir /opt


Summary:  Standalone web browser from mozilla.org, nightly build
Name: firefox-nightly
Version: 110
Release: 0a1%{?dist}
Epoch: 1
License: MPLv1.1 or GPLv2+ or LGPLv2+
Group: Applications/Internet
URL: http://www.mozilla.org/projects/firefox
Source: https://archive.mozilla.org/pub/firefox/nightly/latest-mozilla-central/firefox-%{version}.0a1.en-US.linux-x86_64.tar.bz2

Requires: alsa-lib libX11 libXcomposite libXdamage libnotify libXt libXext glib2 dbus-glib libjpeg-turbo cairo-gobject libffi fontconfig freetype libgcc gtk3 gtk2 hunspell zlib
Requires: nspr >= 4.10.8
Requires: nss >= 3.19.2
Requires: sqlite >= 3.8.10.2

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.
%prep -b
%setup -n firefox
%build

%install
install -dm 755 %{buildroot}/{usr/{bin,share/{applications,pixmaps}},opt}
install -dm 755 %{buildroot}/%{_optdir}/firefox-%{version}/browser/defaults/preferences/

install -m644 %{_builddir}/firefox/browser/chrome/icons/default/default128.png %{buildroot}/usr/share/pixmaps/%{name}-icon.png
cp -rf %{_builddir}/firefox/* %{buildroot}/opt/firefox-%{version}/
ln -s /opt/firefox-%{version}/firefox %{buildroot}/usr/bin/firefox-nightly


cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Firefox Nightly
GenericName=Web Browser
Icon=/usr/share/pixmaps/firefox-nightly-icon.png
Type=Application
Categories=Application;Network;
MimeType=text/html
Encoding=UTF-8
Exec=firefox-nightly %u
Terminal=false
MultipleArgs=false
StartupNotify=false
EOF

cat > %{buildroot}/%{_datadir}/applications/%{name}-safe.desktop << EOF
[Desktop Entry]
Name=Firefox Nightly - Safe Mode
GenericName=Web Browser - Safe Mode
Icon=/usr/share/pixmaps/firefox-nightly-icon.png
Type=Application
Categories=Application;Network;
MimeType=text/html
Encoding=UTF-8
Exec=firefox-nightly -safe-mode %u
Terminal=false
MultipleArgs=false
StartupNotify=false
EOF

# disable update check
#echo '// Disable update check
#pref("app.update.enabled", false);' > %{buildroot}/opt/firefox-%{version}/browser/#defaults/preferences/vendor.js

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/%{name}-icon.png
%{_optdir}/firefox-%{version}/

%changelog
* Wed May 18 2016 Patrik Greco - 49.0a2-1
- rebuilt

* Tue May 17 2016 Patrik Greco <sikevux@sikevux.se> - 49.0a1-1

* Tue Mar 29 2016 David V??squez <davidjeremias82 AT gmail DOT com> - 48.0a1-1
- Updated to 48.0a1

* Mon Aug 10 2015 David V??squez <davidjeremias82 AT gmail DOT com> - 43-0a1
- Initial build
