Name:           ros-indigo-moveit-msgs
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS moveit_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-object-recognition-msgs
Requires:       ros-indigo-octomap-msgs
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-shape-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-object-recognition-msgs
BuildRequires:  ros-indigo-octomap-msgs
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-shape-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs

%description
Messages, services and actions used by MoveIt

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
* Tue Nov 15 2016 Dave Coleman <dave@dav.ee> - 0.7.5-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Dave Coleman <dave@dav.ee> - 0.7.4-0
- Autogenerated by Bloom

* Sat Aug 20 2016 Dave Coleman <dave@dav.ee> - 0.7.3-0
- Autogenerated by Bloom

* Wed Jun 15 2016 Ioan Sucan <isucan@google.com> - 0.7.2-0
- Autogenerated by Bloom

* Wed Apr 13 2016 Ioan Sucan <isucan@google.com> - 0.7.1-0
- Autogenerated by Bloom

* Sat Jan 30 2016 Ioan Sucan <isucan@google.com> - 0.7.0-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Ioan Sucan <isucan@google.com> - 0.6.1-0
- Autogenerated by Bloom

