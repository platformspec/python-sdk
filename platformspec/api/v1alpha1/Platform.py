# generated by datamodel-codegen:
#   filename:  tmpk192mnbf
#   timestamp: 2024-12-07T00:34:57+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ProviderRef(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Dns(BaseModel):
    domain: str = Field(
        ...,
        description='Specifies the top-level domain name associated with this platform.',
    )
    providerRef: ProviderRef = Field(
        ...,
        description='References a Provider resource defining the chosen DNS service (e.g., Route53).',
    )


class Cluster(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Credential(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Environment(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Image(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Network(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Provider(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Server(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class SoftwareGroup(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string\nshould contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].\nFor example, if the object reference is to a container within a pod, this would take on a value like:\n"spec.containers{name}" (where "name" refers to the name of the container that triggered\nthe event) or if no container name is specified "spec.containers[2]" (container with\nindex 2 in this pod). This syntax is chosen only to have some well-defined way of\nreferencing a part of an object.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent.\nMore info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Resources(BaseModel):
    clusters: Optional[List[Cluster]] = Field(
        None,
        description='Defines Kubernetes clusters managed by this platform (if applicable). Each cluster can have its own configuration and deployment parameters.',
    )
    credentials: Optional[List[Credential]] = Field(
        None,
        description='References Credential resources containing the necessary credentials for accessing and interacting with different cloud providers and services.',
    )
    environments: Optional[List[Environment]] = Field(
        None,
        description="Defines different deployment environments (e.g., development, staging, production) for your platform's services and applications.",
    )
    images: Optional[List[Image]] = Field(
        None,
        description='Defines container images used for deploying applications or components within your platform.',
    )
    networks: Optional[List[Network]] = Field(
        None,
        description='References Network resources that define the network configurations used by your platform.',
    )
    providers: Optional[List[Provider]] = Field(
        None,
        description='References Provider resources that define the specific cloud platforms or services used within your environment (e.g., AWS, Azure, GCP).',
    )
    servers: Optional[List[Server]] = Field(
        None,
        description='Lists virtual machines or servers managed within your platform, specifying their configurations and roles.',
    )
    softwareGroups: Optional[List[SoftwareGroup]] = Field(
        None,
        description='Groups together related software packages or dependencies required by various services or applications within your platform.',
    )


class Spec(BaseModel):
    author: Optional[str] = Field(
        None,
        description='The name or team responsible for creating or maintaining this platform.',
    )
    contactEmail: str = Field(
        ...,
        description="An email address for contacting the platform's administrators, maintainers or support team.",
    )
    description: Optional[str] = Field(
        None,
        description="A brief description of the platform's purpose and functionalities.",
    )
    dns: Dns = Field(
        ..., description='Defines the DNS provider and domain used by your platform.'
    )
    organization: str = Field(
        ..., description='The organization responsible for managing this platform.'
    )
    resources: Resources = Field(
        ...,
        description='References to the various resources leveraged or managed by this platform:',
    )
    version: str = Field(
        ...,
        description='A version of the platform, internal to the team defining and managing the platform.',
    )


class Platform(BaseModel):
    apiVersion: Optional[str] = Field(
        'core.platformspec.io/v1alpha1',
        description='APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        'Platform',
        description='Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[Dict[str, Any]] = None
    spec: Optional[Spec] = Field(
        None, description='PlatformSpec defines the desired state of Platform resource.'
    )
    status: Optional[Dict[str, Any]] = Field(
        None, description='PlatformStatus defines the observed state of Platform.'
    )
