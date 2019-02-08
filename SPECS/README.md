# SPECS

In CentOS 7 add epel and scl repositories:

```yum install centos-release-scl-rh epel-release```

Then install gcc-8

```yum --enablerepo=centos-sclo-rh-testing install devtoolset-8-gcc*```

Before build, enable gcc 8

```scl enable devtoolset-8 bash```

```which gcc```

```gcc --version```

Then build the RPM:

```rpmbuild -ba executor.spec```

Enjoy!