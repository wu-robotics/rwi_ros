Name:           ros-hydro-ptu46
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS ptu46 package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/ptu46
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-ptu-control
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-ptu-control
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf

%description
Driver for the Directed Perception ptu46 pan/tilt driver, forked from player

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jul 25 2014 David V. Lu!! <davidvlu@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

