#include <iomanip>
#include <iostream>

using namespace std;


template <typename T>
void extremos(ifstream& f, T& menor, T& mayor){
  T nuevo;
  f.read(reinterpret_cast<char*>(&nuevo), sizeof(T));
  if(!f.eof()){
    if (nuevo < menor) {menor = nuevo:}
    else if (mayor < nuevo) { mayor = nuevo;}
    extremos<T>(f,menor,mayor);
  }
}


/**/
template <typename T>
T primerMenor(cibns char nombre[], cons T limite){
  ifstream f;
  f.open(nombre, ios::binary);
  // bla bla blaaaaaaa..............
}

/*
 * Reforzamiento Precondicion: No se ha leido ningun dato menor que limite hasta el momento
 */
template <typename T>
T primerMenor (ifstream& f, const T limite){
  T new;
  f.read(reinterpret_cast<char*>(&nuevo), sizeof(T));
  if (new < limite){
    return new;
  } else {
    primerMenor(f,T)
  }
}


T UltimoMenor(const char nombre[], const T limite){
  ifstream f;
  f.open(nombre, ios::binary);
  T new;
  f.read(reinterpret_cast<char*>(&nuevo), sizeof(T));
  return UltimoMenor(f, new, limite);
}

/*
 * Reforzamiento Precondicion: El ultimo dato leido <antrior> es menor que limite.
 */
template <typename T>
T UltimoMenor (ifstream& f, const T Anterior, const T limite){
 T new;
 f.read(reinterpret_cast<char*>(&nuevo), sizeof(T));
 if (f.eof()){
   return Anterior;
 } else {
   if (new > limite){
     return Anterior;
   } else {
     return Ultimomenor(f,new,T);
   }
 }
}
