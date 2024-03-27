#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : R-fGarch
Version  : 4033.92
Release  : 53
URL      : https://cran.r-project.org/src/contrib/fGarch_4033.92.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fGarch_4033.92.tar.gz
Summary  : Rmetrics - Autoregressive Conditional Heteroskedastic Modelling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fGarch-lib = %{version}-%{release}
Requires: R-cvar
Requires: R-fBasics
Requires: R-fastICA
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-cvar
BuildRequires : R-fBasics
BuildRequires : R-fastICA
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!-- badges: start -->
[![CRANStatusBadge](http://www.r-pkg.org/badges/version/fGarch)](https://cran.r-project.org/package=fGarch)
[![CRAN RStudio mirror downloads](https://cranlogs.r-pkg.org/badges/fGarch)](https://www.r-pkg.org/pkg/fGarch)
[![CRAN RStudio mirror downloads](https://cranlogs.r-pkg.org/badges/grand-total/fGarch?color=blue)](https://r-pkg.org/pkg/fGarch)
<!-- badges: end -->

%package lib
Summary: lib components for the R-fGarch package.
Group: Libraries

%description lib
lib components for the R-fGarch package.


%prep
%setup -q -n fGarch
pushd ..
cp -a fGarch buildavx2
popd
pushd ..
cp -a fGarch buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711506694

%install
export SOURCE_DATE_EPOCH=1711506694
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fGarch/DESCRIPTION
/usr/lib64/R/library/fGarch/INDEX
/usr/lib64/R/library/fGarch/Meta/Rd.rds
/usr/lib64/R/library/fGarch/Meta/data.rds
/usr/lib64/R/library/fGarch/Meta/features.rds
/usr/lib64/R/library/fGarch/Meta/hsearch.rds
/usr/lib64/R/library/fGarch/Meta/links.rds
/usr/lib64/R/library/fGarch/Meta/nsInfo.rds
/usr/lib64/R/library/fGarch/Meta/package.rds
/usr/lib64/R/library/fGarch/NAMESPACE
/usr/lib64/R/library/fGarch/NEWS.Rd
/usr/lib64/R/library/fGarch/NEWS.md
/usr/lib64/R/library/fGarch/R/fGarch
/usr/lib64/R/library/fGarch/R/fGarch.rdb
/usr/lib64/R/library/fGarch/R/fGarch.rdx
/usr/lib64/R/library/fGarch/THANKS
/usr/lib64/R/library/fGarch/_pkgdown.yml
/usr/lib64/R/library/fGarch/data/Rdata.rdb
/usr/lib64/R/library/fGarch/data/Rdata.rds
/usr/lib64/R/library/fGarch/data/Rdata.rdx
/usr/lib64/R/library/fGarch/help/AnIndex
/usr/lib64/R/library/fGarch/help/aliases.rds
/usr/lib64/R/library/fGarch/help/fGarch.rdb
/usr/lib64/R/library/fGarch/help/fGarch.rdx
/usr/lib64/R/library/fGarch/help/paths.rds
/usr/lib64/R/library/fGarch/html/00Index.html
/usr/lib64/R/library/fGarch/html/R.css
/usr/lib64/R/library/fGarch/pkgdown.yml
/usr/lib64/R/library/fGarch/tests/doRUnit.R
/usr/lib64/R/library/fGarch/unitTests/Makefile
/usr/lib64/R/library/fGarch/unitTests/runTests.R
/usr/lib64/R/library/fGarch/unitTests/runit.bugfix_6061.R
/usr/lib64/R/library/fGarch/unitTests/runit.formula-methods.R
/usr/lib64/R/library/fGarch/unitTests/runit.garch-methods.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.algorithm.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.aparch.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.dist.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.faked.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.garch.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchFit.init.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchHessian.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchSim.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchSolver.R
/usr/lib64/R/library/fGarch/unitTests/runit.garchSpec.R
/usr/lib64/R/library/fGarch/unitTests/runit.plot-methods.R
/usr/lib64/R/library/fGarch/unitTests/runit.predict-methods.R
/usr/lib64/R/library/fGarch/unitTests/runit.sged.R
/usr/lib64/R/library/fGarch/unitTests/runit.snorm.R
/usr/lib64/R/library/fGarch/unitTests/runit.sstd.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/fGarch/libs/fGarch.so
/V4/usr/lib64/R/library/fGarch/libs/fGarch.so
/usr/lib64/R/library/fGarch/libs/fGarch.so
