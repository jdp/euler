(use '[clojure.contrib.math :as math])

(defn pentagonal-number? [x]
  (let [n (/ (+ (math/sqrt (+ (* 24 x) 1)) 1) 6)]
    (= (math/floor n) n)))

(defn hexagonal-number? [x]
  (let [n (/ (+ (math/sqrt (+ (* 8 x) 1)) 1) 4)]
    (= (math/floor n) n)))

(defn triangle-number [n]
  (/ (* n (+ n 1)) 2))

(def triangle-numbers (map #(triangle-number %) (iterate inc 286)))

(println (first (filter #(and (pentagonal-number? %) (hexagonal-number? %)) triangle-numbers)))
