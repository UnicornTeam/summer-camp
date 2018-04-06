INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_BLE_TOOLS BLE_tools)

FIND_PATH(
    BLE_TOOLS_INCLUDE_DIRS
    NAMES BLE_tools/api.h
    HINTS $ENV{BLE_TOOLS_DIR}/include
        ${PC_BLE_TOOLS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    BLE_TOOLS_LIBRARIES
    NAMES gnuradio-BLE_tools
    HINTS $ENV{BLE_TOOLS_DIR}/lib
        ${PC_BLE_TOOLS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(BLE_TOOLS DEFAULT_MSG BLE_TOOLS_LIBRARIES BLE_TOOLS_INCLUDE_DIRS)
MARK_AS_ADVANCED(BLE_TOOLS_LIBRARIES BLE_TOOLS_INCLUDE_DIRS)

