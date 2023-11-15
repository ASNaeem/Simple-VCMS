class Service:
   def __init__(self, name:str, cost:float, service_availability:bool, service_details:str):
      self.name = name
      self.cost = cost
      self.service_availability = service_availability
      self.service_details = service_details

      @property
      def name(self):
         return self._name

      @name.setter
      def name(self, name:str):
         self._name = name

      @property
      def cost(self):
         return self._cost

      @cost.setter
      def cost(self, cost:float):
         self._cost = cost

      @property
      def service_availability(self):
         return self._service_availability

      @service_availability.setter
      def service_availability(self, service_availability:bool):
         self._name = service_availability

      @property
      def service_details(self):
         return self._service_details

      @service_details.setter
      def service_details(self, service_details:str):
         self._service_details = service_details
