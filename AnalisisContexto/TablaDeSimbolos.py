'''
Created on Mar 23, 2016

@author: francisco
'''

class TablaDeSimbolos():
    def __init__(self, upperLevel):
        self.table = dict()
        self.upperLevel = upperLevel
    def __str__(self):
        retorno = ""
        if self.upperLevel is None:
            retorno += "Tabla De Simbolos\n"
            retorno += "    Nivel Superior\n"
            for key in self.table:
                retorno += "        " + key + " ==> " + str(self.getElement(key))
            retorno += "\n"
            return retorno
        else:
            retorno += str(self.upperLevel)
            retorno += "    Siguiente Nivel\n"
            if (self.emptyTable()):
                retorno += "        Nivel Vacio!\n"
            else:
                for key in self.table:
                    retorno += "        " + key + " ==> " + str(self.getElement(key))
            retorno += "\n"
            return retorno
    ''' Funciones simples de primer nivel '''
    def agregarATabla(self,key,element):
        self.table.update({key: element})
        return self
    def emptyTable(self):
        if (self.table):
            return False
        else:
            return True
    def getElement(self,key):
        return self.table.get(key)
    def obtenerNivelSuperior(self):
        return self.upperLevel
    def getTable(self):
        return self.table
    ''' Funciones Complejas Recursivas '''
    def buscarSimbolo(self,identifier):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        retorna el simbolo
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @rtype:   Object
        @return:  El valor del simbolo encontrado
        """
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            return element
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.obtenerNivelSuperior() is None:
                return None;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.obtenerNivelSuperior().buscarSimbolo(identifier)
            
    def actualizarValorDeSimbolo(self,identifier,valor):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        actualiza su valor
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @type  valor: Object
        @param valor: nuevo valor
        @rtype:   TablaDeSimbolos
        @return:  La tabla actualizada
        """
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            element = element.setValue(valor)
            self.table.update({identifier: element})
            return True
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.obtenerNivelSuperior() is None:
                return False;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.obtenerNivelSuperior().actualizarValorDeSimbolo(identifier,valor)

    def actualizarPosicionHorSimbolo(self,identifier,horPosicion):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        actualiza su posicion horizontal
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @type  horPosicion: int
        @param horPosicion: nueva posicion horizontal
        @rtype:   TablaDeSimbolos
        @return:  La tabla actualizada
        """
   
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            element.horPosicion = horPosicion
            self.table.update({identifier: element})
            return True
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.obtenerNivelSuperior() is None:
                return False;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.obtenerNivelSuperior().actualizarPosicionHorSimbolo(identifier,horPosicion)


    def actualizarPosicionVerSimbolo(self,identifier,verPosicion):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        actualiza su posicion vertical
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @type  verPosicion: int
        @param verPosicion: nueva posicion vertical
        @rtype:   TablaDeSimbolos
        @return:  La tabla actualizada
        """
   
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            element.verPosicion = verPosicion
            self.table.update({identifier: element})
            return True
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.obtenerNivelSuperior() is None:
                return False;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.obtenerNivelSuperior().actualizarPosicionVerSimbolo(identifier,verPosicion)

    def actualizarEstadoSimbolo(self,identifier,status):
        """
        Busca un elemento en los distintos niveles de la tabla de simbolos y 
        actualiza su estado
        
        Si el valor no se encuentra, retorna None
        
        @type  identifier: String
        @param identifier: Nombre del simbolo a buscar
        @type  status: bool
        @param status: estado nuevo
        @rtype:   TablaDeSimbolos
        @return:  La tabla actualizada
        """
   
        # Buscamos el simbolo
        element = self.getElement(identifier)
        # Caso 1: Se encuentra, se devuelve el valor del simbolo
        if (element is not None):
            element.activado = status
            self.table.update({identifier: element})
            return True
        # Caso 2: No se encuentra, se busca en la tabla de nivel superior
        else:
            # Caso 2.1: Estamos en el ultima nivel, el elemento no existe en la tabla
            # asi que retornamos None
            if self.obtenerNivelSuperior() is None:
                return False;
            # Caso 2.2: No estamos en el ultimo nivel, buscamos en el nivel superior
            else:
                return self.obtenerNivelSuperior().actualizarEstadoSimbolo(identifier,status)

