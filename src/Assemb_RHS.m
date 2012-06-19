function [rhs grad_rhs] = Assemb_RHS(t, p, z1, z2)
	x = p(:, 1); 
	y = p(:, 2);

	N_elements = length(t(:, 1));
	N_points = length(p(:, 1));
	rhs = zeros(N_points, 1);
	grad_rhs_1 = zeros(N_points, 1);
	grad_rhs_2 = zeros(N_points, 1);

	for el = 1:N_elements
		[b_el, b_el_dz1, b_el_dz2] = Element_Vector(t, p, el, z1, z2);
		rhs(t(el,1:3)) = rhs(t(el,1:3)) + b_el;
		grad_rhs_1(t(el,1:3)) = grad_rhs_1(t(el,1:3)) + b_el_dz1;
		grad_rhs_2(t(el,1:3)) = grad_rhs_2(t(el,1:3)) + b_el_dz2;
	end

	grad_rhs = [grad_rhs_1 grad_rhs_2];

end
