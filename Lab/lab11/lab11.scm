(define (make-even t) 
    (
        if (= (modulo (label t) 2) 1)
            (tree (+ (label t) 1) (map (lambda (b) (make-even b)) (branches t)))
            (tree (label t) (map (lambda (b) (make-even b)) (branches t)))
    )
)

(define (find t x) 
    (
        if (= (label t) x)
            #t
            (> (length (filter (lambda (b) (find b x)) (branches t))) 0)
    )

)

(define (n-ary t n) 
    (if (is-leaf t) #t
        (and
            (= (length (branches t)) n )
            (= (length (filter (lambda (b) (n-ary b n))(branches t))) n)            
        )
    )
)
