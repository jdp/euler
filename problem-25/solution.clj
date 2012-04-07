(ns euler-25)

(def fib (memoize (fn [n] 
  (if (< n 2)
    n
    (+ (fib (- n 1)) (fib (- n 2)))))))
    
(println (+ 1 (count (take-while #(< (.length (str %)) 1000) (map fib (iterate inc 1))))))