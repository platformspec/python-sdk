# generated by datamodel-codegen:
#   filename:  tmpylpppkoa
#   timestamp: 2024-12-07T00:34:56+00:00

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


class Spec(BaseModel):
    description: Optional[str] = Field(
        None,
        description="Provides a concise description of the environment's purpose and intended use.",
    )
    providerRefs: List[ProviderRef] = Field(
        ...,
        description='References specific Provider resources that define the cloud platforms or services used within this environment. This ensures that the correct configurations and credentials are applied based on the target environment.',
    )


class Environment(BaseModel):
    apiVersion: Optional[str] = Field(
        'core.platformspec.io/v1alpha1',
        description='APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        'Environment',
        description='Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[Dict[str, Any]] = None
    spec: Optional[Spec] = Field(
        None, description='EnvironmentSpec defines the desired state of Environment.'
    )
    status: Optional[Dict[str, Any]] = Field(
        None, description='EnvironmentStatus defines the observed state of Environment.'
    )