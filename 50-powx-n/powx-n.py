class Solution:
    def myPow(self, x: float, n: int) -> float:


      
      def myPow2(x: float, n: int) -> float:

         if n==0:
            return 1
         elif n==1:
            return x

         print(x,n)
         if n%2==0:
            u= myPow2( x,int(n/2))
            return u*u
         else:
            u= myPow2( x,int(n/2))
            return u*u*x


      p= myPow2(x, n)

      if n >0:
         return p
      else:
         return (1/p)


        