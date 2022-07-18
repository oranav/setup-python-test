cmake_minimum_required(VERSION 3.10)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/modules")
find_package(Libffi REQUIRED)

project(ffi)

add_library(somelib MODULE somelib/somelib.c)

add_executable(main main.c)

add_executable(mainffi mainffi.c)

target_include_directories(main PUBLIC
	"${PROJECT_SOURCE_DIR}/somelib"
	)
target_link_libraries(main ${CMAKE_DL_LIBS})

target_include_directories(mainffi PUBLIC
	"${PROJECT_SOURCE_DIR}/somelib"
	)
target_link_libraries(mainffi PRIVATE ${LIBFFI_LIBRARY} ${CMAKE_DL_LIBS})
