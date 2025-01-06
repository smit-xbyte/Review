from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmployeeReview
from .excel_utils import save_to_excel
import datetime

def user_add_review(request):
    current_month = datetime.datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        try:
            # Extract form data directly from POST
            email = request.POST.get('email')
            emp_id = request.POST.get('emp-id')
            developer_name = request.POST.get('developer-name')
            team_leader = request.POST.get('team-leader')
            project_manager = request.POST.get('project-manager')
            review_month = request.POST.get('review-month')
            delivery_timelines = request.POST.get('delivery-timelines')
            utilization = request.POST.get('utilization')
            technology = request.POST.get('technology')
            attitude = request.POST.get('attitude')
            code_quality = request.POST.get('code-quality')
            communication = request.POST.get('communication')
            glacier_process = request.POST.get('glacier-process')
            bugs = request.POST.get('bugs')
            attendance = request.POST.get('attendance')
            outstanding = request.POST.get('outstanding')
            rating = request.POST.get('rating')

            remarks = request.POST.get('remarks')

            # Basic Validation: Check if required fields are provided
            required_fields = [email, emp_id, developer_name, review_month]
            if any(field is None or field == "" for field in required_fields):
                messages.error(request, "Please fill in all required fields.")
                return render(request, 'form.html',{'current_month': current_month})

            # Save the data to the database
            review = EmployeeReview(
                email=email,
                emp_id=emp_id,
                developer_name=developer_name,
                team_leader=team_leader,
                project_manager=project_manager,
                review_month=review_month,
                delivery_timelines=delivery_timelines,
                utilization=utilization,
                technology=technology,
                attitude=attitude,
                code_quality=code_quality,
                communication=communication,
                glacier_process=glacier_process,
                bugs=bugs,
                attendance=attendance,
                outstanding=outstanding,
                rating=rating,
                remarks=remarks,
            )

            review.save()

            save_to_excel([review])
            # Redirect to a "Thank You" page
            messages.success(request, "Review submitted successfully!")
            return render(request, 'thankyou.html')

        except Exception as e:
            # Handle unexpected errors
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'form.html',{'current_month': current_month})

    return render(request, 'form.html',{'current_month': current_month})
