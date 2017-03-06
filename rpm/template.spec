Name:           ros-indigo-rospack
Version:        2.2.8
Release:        0%{?dist}
Summary:        ROS rospack package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rospack
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       pkgconfig
Requires:       python-catkin_pkg
Requires:       python-devel
Requires:       python-rosdep
Requires:       tinyxml-devel
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig
BuildRequires:  python-coverage
BuildRequires:  python-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  tinyxml-devel

%description
ROS Package Tool

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 2.2.8-0
- Autogenerated by Bloom

* Mon Jun 27 2016 Dirk Thomas <dthomas@osrfoundation.org> - 2.2.7-0
- Autogenerated by Bloom

* Wed Mar 09 2016 Dirk Thomas <dthomas@osrfoundation.org> - 2.2.6-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Dirk Thomas <dthomas@osrfoundation.org> - 2.2.5-0
- Autogenerated by Bloom

