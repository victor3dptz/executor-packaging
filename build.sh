#!/bin/bash

rpmbuild -ba ./SPECS/executor.spec
rpmbuild -ba ./SPECS/executor-aux.spec