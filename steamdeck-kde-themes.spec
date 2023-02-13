Name:           steamdeck-kde-themes
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        KDE Themes from Valve's SteamOS 3.0
License:    	GPLv2
URL:            https://github.com/KyleGospo/steamdeck-kde-presets

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}
BuildArch:      noarch

Requires:		kde-filesystem

%description
KDE Themes from Valve's SteamOS 3.0

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{buildroot}%{_datadir}/
cp -rv usr/share/* %{buildroot}%{_datadir}

# Remove unneeded files
rm %{buildroot}%{_datadir}/applications/org.mozilla.firefox.desktop
rm -rf %{buildroot}%{_datadir}/kservices5
rm -rf %{buildroot}%{_datadir}/X11

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%{_datadir}/color-schemes/*
# %%{_datadir}/X11/*
# %%{_datadir}/applications/org.mozilla.firefox.desktop
%{_datadir}/icons/*
%{_datadir}/konsole/*
# %%{_datadir}/kservices5/*
%{_datadir}/plasma/avatars/*
%{_datadir}/plasma/desktoptheme/*
%{_datadir}/plasma/look-and-feel/com.valve.vapor.desktop/*
%{_datadir}/plasma/look-and-feel/com.valve.vgui.desktop/*
%{_datadir}/themes/*
%{_datadir}/wallpapers/*

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}