#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fGarch
Version  : 3042.83
Release  : 3
URL      : https://cran.r-project.org/src/contrib/fGarch_3042.83.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fGarch_3042.83.tar.gz
Summary  : Rmetrics - Autoregressive Conditional Heteroskedastic Modelling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fGarch-lib
Requires: R-fBasics
Requires: R-fastICA
Requires: R-timeDate
BuildRequires : R-fBasics
BuildRequires : R-fastICA
BuildRequires : R-timeDate
BuildRequires : clr-R-helpers

%description
analyze and model heteroskedastic behavior in financial time
  series models.

%package lib
Summary: lib components for the R-fGarch package.
Group: Libraries

%description lib
lib components for the R-fGarch package.


%prep
%setup -q -c -n fGarch

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530461549

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530461549
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fGarch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fGarch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fGarch
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fGarch|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/fGarch/R/fGarch
/usr/lib64/R/library/fGarch/R/fGarch.rdb
/usr/lib64/R/library/fGarch/R/fGarch.rdx
/usr/lib64/R/library/fGarch/THANKS
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
/usr/lib64/R/library/fGarch/libs/symbols.rds
/usr/lib64/R/library/fGarch/unitTests/Makefile
/usr/lib64/R/library/fGarch/unitTests/runTests.R
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
/usr/lib64/R/library/fGarch/libs/fGarch.so
/usr/lib64/R/library/fGarch/libs/fGarch.so.avx2
/usr/lib64/R/library/fGarch/libs/fGarch.so.avx512
