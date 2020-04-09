py_library(
    name = "package_b",
    srcs = ["module4.py"],
    imports = [".."],
    # imports = ["//custom_project_root"],
    srcs_version = "PY3",
    visibility = ["//custom_project_root:__subpackages__"],
    deps = [
        "//custom_project_root/package_a",
        "//custom_project_root/package_a/package_b",
    ],
)
