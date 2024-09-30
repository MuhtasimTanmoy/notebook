# Xcodeproj

Here is the list of elements contained in the file format:

- Root Element

- PBXBuildFile
    - This element indicates a file reference that is used in a PBXBuildPhase (either as an include or resource).

- PBXBuildPhase - This element is an abstract parent for specialized build phases.
    - PBXAppleScriptBuildPhase
    - PBXCopyFilesBuildPhase
        - This is the element for the copy file build phase.
    - PBXFrameworksBuildPhase
    - PBXHeadersBuildPhase
        - This is the element for the framework link build phase.
    - PBXResourcesBuildPhase
        - This is the element for the resources copy build phase.
    - PBXShellScriptBuildPhase
        - This is the element for the resources copy build phase.
    - PBXSourcesBuildPhase
        - This is the element for the sources compilation build phase.
        
- PBXContainerItemProxy
    - This is the element for to decorate a target item.

- PBXFileElement - This element is an abstract parent for file and group elements.
    - PBXFileReference
        - A PBXFileReference is used to track every external file referenced by the project: source files, resource files, libraries, generated application files, and so on.
    - PBXGroup
        - This is the element to group files or groups.
    - PBXVariantGroup
        - This is the element for referencing localized resources.

- PBXTarget
    - PBXAggregateTarget
        - This is the element for a build target that aggregates several others.
    - PBXLegacyTarget
    - PBXNativeTarget
        - This is the element for a build target that produces binary content (application or library).

- PBXProject
    - This is the element for a build target that produces binary content (application or library).

- PBXTargetDependency
    - This is the element for referencing another target through content proxies.

- XCBuildConfiguration

- XCConfigurationList
    - This is the element for listing build configurations.

- Remove Occurrences of null
    - `sed -i '' '/(null) in Sources /d' YOURPROJECT.xcodeproj/project.pbxproj`
    - `sed -i '' '/(null) in Resources /d' ProjectName.xcodeproj/project.pbxproj`
    - `sed -i '' '/(null) in Frameworks /d' ProjectName.xcodeproj/project.pbxproj`