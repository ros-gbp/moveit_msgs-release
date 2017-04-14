Name:           ros-lunar-moveit-msgs
Version:        0.9.1
Release:        0%{?dist}
Summary:        ROS moveit_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-actionlib-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-object-recognition-msgs
Requires:       ros-lunar-octomap-msgs
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-shape-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-trajectory-msgs
BuildRequires:  ros-lunar-actionlib-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-object-recognition-msgs
BuildRequires:  ros-lunar-octomap-msgs
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-shape-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-trajectory-msgs

%description
Messages, services and actions used by MoveIt

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Apr 14 2017 Dave Coleman <dave@dav.ee> - 0.9.1-0
- Autogenerated by Bloom

