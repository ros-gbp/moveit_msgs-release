%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-moveit-msgs
Version:        0.11.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_msgs package

License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-generation
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-object-recognition-msgs
Requires:       ros-noetic-octomap-msgs
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-shape-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-trajectory-msgs
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-object-recognition-msgs
BuildRequires:  ros-noetic-octomap-msgs
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-shape-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Messages, services and actions used by MoveIt

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Aug 19 2020 Dave Coleman <dave@dav.ee> - 0.11.0-1
- Autogenerated by Bloom

