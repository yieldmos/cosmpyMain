"""Interface for the Staking functionality of CosmosSDK."""

from abc import ABC, abstractmethod

from cosmos.staking.v1beta1.query_pb2 import (
    QueryDelegationRequest,
    QueryDelegationResponse,
    QueryDelegatorDelegationsRequest,
    QueryDelegatorDelegationsResponse,
    QueryDelegatorUnbondingDelegationsRequest,
    QueryDelegatorUnbondingDelegationsResponse,
    QueryDelegatorValidatorRequest,
    QueryDelegatorValidatorResponse,
    QueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse,
    QueryHistoricalInfoRequest,
    QueryHistoricalInfoResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryPoolRequest,
    QueryPoolResponse,
    QueryRedelegationsRequest,
    QueryRedelegationsResponse,
    QueryUnbondingDelegationRequest,
    QueryUnbondingDelegationResponse,
    QueryValidatorDelegationsRequest,
    QueryValidatorDelegationsResponse,
    QueryValidatorRequest,
    QueryValidatorResponse,
    QueryValidatorsRequest,
    QueryValidatorsResponse,
    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorUnbondingDelegationsResponse,
)


class Staking(ABC):
    """Staking abstract class."""

    @abstractmethod
    def Validators(self, request: QueryValidatorsRequest) -> QueryValidatorsResponse:
        """Validators queries all validators that match the given status."""

    @abstractmethod
    def Validator(self, request: QueryValidatorRequest) -> QueryValidatorResponse:
        """Validator queries validator info for given validator address."""

    @abstractmethod
    def ValidatorDelegations(
        self, request: QueryValidatorDelegationsRequest
    ) -> QueryValidatorDelegationsResponse:
        """ValidatorDelegations queries delegate info for given validator."""

    @abstractmethod
    def ValidatorUnbondingDelegations(
        self, request: QueryValidatorUnbondingDelegationsRequest
    ) -> QueryValidatorUnbondingDelegationsResponse:
        """ValidatorUnbondingDelegations queries unbonding delegations of a validator."""

    @abstractmethod
    def Delegation(self, request: QueryDelegationRequest) -> QueryDelegationResponse:
        """Delegation queries delegate info for given validator delegator pair."""

    @abstractmethod
    def UnbondingDelegation(
        self, request: QueryUnbondingDelegationRequest
    ) -> QueryUnbondingDelegationResponse:
        """UnbondingDelegation queries unbonding info for given validator delegator pair."""

    @abstractmethod
    def DelegatorDelegations(
        self, request: QueryDelegatorDelegationsRequest
    ) -> QueryDelegatorDelegationsResponse:
        """DelegatorDelegations queries all delegations of a given delegator address."""

    @abstractmethod
    def DelegatorUnbondingDelegations(
        self, request: QueryDelegatorUnbondingDelegationsRequest
    ) -> QueryDelegatorUnbondingDelegationsResponse:
        """DelegatorUnbondingDelegations queries all unbonding delegations of a given delegator address."""

    @abstractmethod
    def Redelegations(
        self, request: QueryRedelegationsRequest
    ) -> QueryRedelegationsResponse:
        """Redelegations queries redelegations of given address."""

    @abstractmethod
    def DelegatorValidators(
        self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponse:
        """DelegatorValidators queries all validators info for given delegator address."""

    @abstractmethod
    def DelegatorValidator(
        self, request: QueryDelegatorValidatorRequest
    ) -> QueryDelegatorValidatorResponse:
        """DelegatorValidator queries validator info for given delegator validator pair."""

    @abstractmethod
    def HistoricalInfo(
        self, request: QueryHistoricalInfoRequest
    ) -> QueryHistoricalInfoResponse:
        """HistoricalInfo queries the historical info for given height."""

    @abstractmethod
    def Pool(self, request: QueryPoolRequest) -> QueryPoolResponse:
        """Pool queries the pool info."""

    @abstractmethod
    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """Parameters queries the staking parameters."""