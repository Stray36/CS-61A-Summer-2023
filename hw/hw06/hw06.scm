(define (no-repeats lst) 
  (if (null? lst) 
    nil
    (cons (car lst) (no-repeats (filter(lambda (x) (not (= x (car lst)))) (cdr lst))))
  )
)

(define (student-attend-class student class)
  (student-create (student-get-name student) (cons class (student-get-classes student)) )
)

(define (teacher-hold-class teacher)
  (define updated-students
  (map (lambda (student)
  (student-attend-class student (teacher-get-class teacher)))
  (teacher-get-students teacher)))

  (teacher-create (teacher-get-name teacher) (teacher-get-class teacher) updated-students)
)

(define (add-leaf t x)
  (if (is-leaf t)
      t
      (begin (define mapped-branches
                  (map (lambda (b) (add-leaf b x)) (branches t)))
             (tree (label t)
                  (append mapped-branches (list(tree x nil)))))))
